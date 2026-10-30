#!/usr/bin/env python3
"""Check this package's narrow metadata format, links and disclosure clues."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
NAMES = ("hyhj-frontend-dev", "hyhj-backend-dev")
TEXT_EXTENSIONS = {".md", ".yaml", ".yml", ".py"}
IGNORED = {".git", "__pycache__"}


def quoted_field(text, key):
    match = re.search(r"^" + re.escape(key) + r': ("[^\n]*")$', text, re.M)
    if not match:
        raise ValueError("missing quoted field: " + key)
    return json.loads(match.group(1))


def within(path, directory):
    try:
        path.relative_to(directory)
        return True
    except ValueError:
        return False


def check(root):
    root = root.resolve()
    errors = []
    all_files = sorted(p for p in root.rglob("*")
                       if not any(part in IGNORED for part in p.relative_to(root).parts))
    for path in all_files:
        label = str(path.relative_to(root))
        if path.is_symlink():
            errors.append(label + ": symlinks are not shipped")
            continue
        if not path.is_file():
            continue
        if path.suffix not in TEXT_EXTENSIONS and path.name not in {"LICENSE", ".gitignore"}:
            errors.append(label + ": unexpected file type")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(label + ": not UTF-8 text")
            continue
        # These are clues, not a guarantee that text is safe to publish.
        clues = {
            "local absolute path": r"(?:/Users/|/home/)[A-Za-z0-9_.-]+/",
            "private IPv4 address": r"(?<![\d.])(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})(?![\d.])",
            "credential in URL": r"https?://[^\s/@:]+:[^\s/@]+@",
            "private key": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
            "credential-like token": r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9_-]{24,})\b",
            "unfinished scaffold": r"\[TODO:",
            "vault-only link": r"\[\[[^\n]+\]\]",
        }
        for reason, pattern in clues.items():
            if reason == "unfinished scaffold" and path.suffix != ".md":
                continue
            if re.search(pattern, content):
                errors.append(label + ": " + reason)
        if path.suffix != ".md":
            continue
        skill_root = None
        for name in NAMES:
            candidate = root / "skills" / name
            if within(path, candidate):
                skill_root = candidate
                break
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", content):
            target = target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme in {"https", "http", "mailto"}:
                continue
            if parsed.scheme or parsed.netloc:
                errors.append(label + ": unsupported link " + target)
                continue
            if not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            boundary = skill_root or root
            if not within(destination, boundary):
                errors.append(label + ": link leaves installable boundary " + target)
            elif not destination.is_file():
                errors.append(label + ": missing linked file " + target)

    for name in NAMES:
        skill = root / "skills" / name
        entry = skill / "SKILL.md"
        if not entry.is_file():
            errors.append(name + ": missing SKILL.md")
            continue
        content = entry.read_text(encoding="utf-8")
        parts = content.split("---\n", 2)
        if len(parts) != 3 or parts[0]:
            errors.append(name + ": invalid frontmatter delimiters")
            continue
        # This package deliberately uses only two simple frontmatter fields.
        fields = {}
        for line in parts[1].strip().splitlines():
            if ": " not in line:
                errors.append(name + ": unsupported frontmatter format")
                continue
            key, value = line.split(": ", 1)
            if key in fields:
                errors.append(name + ": duplicate metadata field " + key)
            fields[key] = value
        if fields.get("name") not in {name, json.dumps(name)}:
            errors.append(name + ": metadata name does not match directory")
        if set(fields) != {"name", "description"}:
            errors.append(name + ": expected name and description fields")
        description = fields.get("description", "").strip().strip('"')
        if not description or len(description) > 1024:
            errors.append(name + ": invalid description length")
        metadata = skill / "agents" / "openai.yaml"
        try:
            ui = metadata.read_text(encoding="utf-8")
            for field in ("display_name", "short_description", "default_prompt"):
                value = quoted_field(ui, "  " + field)
                if not value:
                    raise ValueError("empty UI field " + field)
            short = quoted_field(ui, "  short_description")
            if not 25 <= len(short) <= 64:
                raise ValueError("short_description must contain 25 to 64 characters")
            if "$" + name not in quoted_field(ui, "  default_prompt"):
                raise ValueError("default_prompt does not invoke its skill")
            if re.search(r"allow_implicit_invocation:\s*false", ui):
                raise ValueError("automatic discovery must remain enabled")
            if re.search(r"^dependencies:", ui, re.M):
                raise ValueError("this package has no hard tool dependencies")
        except (OSError, ValueError) as exc:
            errors.append(name + ": " + str(exc))

    common = [root / "skills" / n / "references" / "skill-selection.md" for n in NAMES]
    if not all(p.is_file() for p in common):
        errors.append("missing shared skill-selection reference")
    elif common[0].read_bytes() != common[1].read_bytes():
        errors.append("skill-selection references have diverged")
    for name in ("README.md", "LICENSE", "SOURCES.md"):
        if not (root / name).is_file():
            errors.append("missing distribution file " + name)
    return errors


def main():
    errors = check(ROOT)
    if errors:
        for error in errors:
            print("FAIL " + error)
        return 1
    print("PASS metadata, local links, independent skill boundaries, shared references and disclosure clues")
    print("Manual disclosure review and task-level verification remain necessary.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
