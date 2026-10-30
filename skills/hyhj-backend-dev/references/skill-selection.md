# 技能选用与 Matt Compound 对照

只在选择开发流程、检查可用增强技能，或解释两者区别时读取本页。普通实现直接使用入口内的工作流，不为读完工具目录而延迟交付。

## 共同原则

本 skill 自身提供开发流程，第三方 skill 只是可选增强。先检查当前宿主实际提供的技能和项目约定；名字相似不代表能力、版本和调用策略相同。未安装时使用现有工具完成任务，不能声称调用了不存在的 skill。

一项任务选择一套主要流程，复用已有需求、计划和验证结果。不把 Matt 和 Compound 的两套完整流程串行重复执行，也不因工具偏好改变用户已确认的行为或范围。

外部技能的自动调用、显式调用与操作权限遵守当前宿主规则。手动专用技能不能绕过其调用限制。只有需要安装且处于任务授权范围时才进行安装，安装前核验官方说明、维护状态与许可证；不要多渠道重复安装同一套技能。

## 两者的主要区别

Matt 与 Compound Engineering 都覆盖需求、规格或计划、实施、测试、调试、架构与审查，两者也都有并行实现或审查能力。

| 比较点 | Matt | Compound Engineering |
|---|---|---|
| 组织方式 | 小型、可组合的工程方法，按需要挑选 | 围绕开发闭环衔接各阶段，明确输入与完成条件 |
| 需求和计划 | 共享领域词汇、架构决策、规格与带依赖的任务 | 需求讨论与规划可以逐步完善同一份统一计划，用稳定编号追踪需求、工作与验收 |
| 实现重点 | 小步实现、TDD、清晰模块接口和可测试边界 | 按计划实施，独立提供简化检查，再开展审查与验证 |
| 经验回流 | 领域词汇和决策记录；retro 改善 AI 的工作环境 | ce-compound 保存有长期价值的项目推理，供后续规划与审查读取 |
| 自动交付 | 有实施、提交、任务图并行实现和并行审查 | 另有 lfg 集成开发、验证、提交、推送、PR 与 CI 跟进 |
| 使用成本 | 取决于实际启用的流程与任务范围 | 完整闭环涉及更多约定和产物，同时支持轻量路径 |

这是一组侧重点，不是能力高低或性能排名。不能断言 Matt 一定更快、更省 token，也不能要求 Compound 每次都走完整流程。

## 按任务选用

| 当前需要 | 可以复用的增强能力 |
|---|---|
| 产品行为不清楚 | Matt 的 grill-with-docs 或 Compound 的 ce-brainstorm，选择一种 |
| 已明确需求，需要可执行范围与验收 | Matt 的 to-spec / to-tickets，或 Compound 的 ce-plan；沿用已有规格 |
| 实施与测试 | Matt 的 tdd / implement，或 Compound 的 ce-work；根据任务和现有测试选择 |
| 缺陷定位 | Matt 的 diagnosing-bugs 或 Compound 的 ce-debug；先复现再修复 |
| 质量检查 | Matt 的 code-review，或 Compound 的 ce-simplify-code / ce-code-review，使用适合当前差异的检查 |
| 改善 AI 工作环境 | Matt 的 retro，检查导航、自动检查和规则的实际问题 |
| 保存难以从代码理解的长期经验 | Compound 的 ce-compound；先确认经验非显而易见、长期有用且值得保存 |
| 明确要求自动交付 | 评估 lfg 与当前权限、测试和仓库条件；自动交付不代表自动合并或生产部署 |

TDD 用于验证业务行为和防止回归，不机械套用于每次文案、颜色或低影响样式修改。复盘也不等于每次生成文档：能用测试、类型、局部注释或现有文档表达的知识，放在最适合的位置。

## 前端可选补充

有界面开发时，可按需使用 Emil 的 emil-design-eng 和 pick-ui-library；已有组件库时优先沿用。涉及动效才考虑 review-animations、find-animation-opportunities 等能力。apple-design 可以帮助判断即时反馈和连续交互，不规定所有产品采用 Apple 视觉风格。

## 来源

下列官方资料于 2026-10-30 对照阅读。实际调用前以宿主可用能力与相应版本的说明为准。

- [Matt 官方说明与技能列表](https://github.com/mattpocock/skills)
- [Matt retro](https://github.com/mattpocock/skills/blob/main/skills/engineering/retro/SKILL.md)
- [Compound Engineering 官方说明](https://github.com/EveryInc/compound-engineering-plugin)
- [Compound 计划衔接](https://github.com/EveryInc/compound-engineering-plugin/blob/main/docs/guides/ce-plan.md)
- [Compound 经验沉淀](https://github.com/EveryInc/compound-engineering-plugin/blob/main/docs/guides/ce-compound.md)
- [Emil 设计工程技能](https://github.com/emilkowalski/skills)
