# HYHJ 开发 Skills

两套可独立安装的中文开发 skill，把个人开发规范转成 AI 可以执行的工作流程：沿用项目现状，先明确必要的需求与验收，小步实现，用实际结果验证，并保留有价值的经验。

| Skill | 适用任务 | 内容入口 |
|---|---|---|
| `hyhj-frontend-dev` | Web 页面、组件、交互、响应式适配和前端缺陷 | [前端 SKILL.md](skills/hyhj-frontend-dev/SKILL.md) |
| `hyhj-backend-dev` | 服务端接口、业务规则、数据持久化、后台任务和后端缺陷 | [后端 SKILL.md](skills/hyhj-backend-dev/SKILL.md) |

它们不要求安装 Matt、Compound Engineering 或 Emil。已有这些能力时可以按需使用；没有时按 skill 自带流程完成工作。接手已有项目先识别其技术栈和规则，不默认更换框架、数据库或目录结构。

## 安装到 Codex

先下载或克隆本仓库，再进入本目录。每个 skill 的整个文件夹都需要保留，包括 `references`、`agents` 和许可证。

```sh
git clone https://github.com/H-YHJ/hyhj-dev-skills.git
cd hyhj-dev-skills
```

Codex 当前支持项目级 `.agents/skills` 和用户级 `~/.agents/skills`，详见 [官方技能文档](https://learn.chatgpt.com/docs/build-skills)。以下示例用于首次安装前端 skill，目标已存在时不会覆盖：

```sh
skill_dest="$HOME/.agents/skills/hyhj-frontend-dev"
if [ -e "$skill_dest" ] || [ -L "$skill_dest" ]; then
  printf '%s\n' '目标已存在，请先比较已有版本，再决定更新。'
else
  mkdir -p "$(dirname "$skill_dest")"
  cp -R skills/hyhj-frontend-dev "$skill_dest"
fi
```

安装后端时，将示例中的两处 `hyhj-frontend-dev` 换为 `hyhj-backend-dev`。项目级安装则将目标改为目标代码仓库的 `.agents/skills/技能名`，不要误装到当前资料仓库。自定义或旧版宿主若使用其他目录，以该宿主的实际说明为准。

Codex 会发现新技能；没有显示时重启再检查。可以显式调用，也允许按任务自动匹配。不要在用户级、项目级和插件中重复安装同名技能。[发现与调用说明](https://learn.chatgpt.com/docs/build-skills)

本仓库提供直接 skill 文件夹，未附带插件 marketplace 或 MCP 服务。其他兼容 Agent Skills 的宿主可以复制对应文件夹，但调用语法和安装位置按宿主说明处理。

## 怎么使用

在目标代码仓库中调用，例如：

```text
使用 $hyhj-frontend-dev 修复相册快速切图时旧图片覆盖新选择的问题，
沿用现有组件和样式，完成实现与针对性验证。
```

```text
使用 $hyhj-backend-dev 为现有创建接口补充幂等处理，
保持对外契约，验证权限、重复请求和真实数据库持久化。
```

```text
使用 $hyhj-frontend-dev 和 $hyhj-backend-dev 完成这个全栈功能。
先明确接口与页面验收，再按各自职责实施，共用一份必要的计划。
```

如果只需要方案，明确说“先出方案，不改代码”。自动匹配不会替用户决定发布、购买服务或进行破坏性迁移；实际行动遵守当前任务已有授权。

## 工作方式

- 只询问影响产品行为、公开范围、成本或重要业务边界的未决问题；可由项目证据确定的工程事项主动推进，已确认的决定持续沿用。
- 小改动做针对性验证；普通功能连接需求与验收；影响权限、持久化或外部契约的改动补充失败处理与恢复方案。
- 页面功能必须能实际操作；后端不能用内存或 mock 结果冒充真实集成成功。工具受限时说明未验证范围。
- 每次任务选择一套主要流程，避免同时完整执行多套需求、计划与审查流程。
- 详细参考只在相关任务中读取，两个 skill 均不依赖另一个 skill 或本仓库根目录才能运行。

Matt 与 Compound 的对照、推荐增强技能和选择方式见各 skill 内的 [技能选用说明](skills/hyhj-frontend-dev/references/skill-selection.md)。前端界面质量可按需使用 Emil；动效规则不等于默认采用 Apple 视觉风格。

## 维护与检查

运行本仓库的本地检查，无需安装第三方 Python 包：

```sh
python3 scripts/check.py
```

需要 Python 3.9 或以上。检查覆盖本仓库约定的元数据、引用是否存在、技能安装独立性、共用参考的一致性，以及常见敏感信息线索；它不代替人工脱敏审查或实际任务验证。GitHub Actions 使用同一检查入口。

更新时修改相关参考，保持两个 `skill-selection.md` 内容同步，重新运行检查，再用受影响的真实任务验证。版本与许可证查证记录见 [SOURCES.md](SOURCES.md)。

本版结构检查、独立任务试用与未覆盖范围见 [VALIDATION.md](VALIDATION.md)。

## GitHub 发布

公开内容只包括本目录。先检查待上传文件，再将本目录作为独立仓库上传；不要在上层知识库执行全量添加。

发布前确认示例已虚构化、没有内部业务映射或私人资料，检查通过，并复核许可证和公开范围。技能制作、安装、GitHub 发布和生产部署是不同操作，沿用各操作在当前任务中已有的授权。

本项目采用 [MIT License](LICENSE)。第三方方法以来源链接介绍，未打包第三方完整 skill。项目资料仅提炼通用方法，公开文件不包含原始内部资料。
