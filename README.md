# PBDD

中文 | [English](README.en.md)

**PBDD（Project Brain Driven Development）是一套开放规范，用于让 AI Agent 以统一协议维护项目状态、执行工程流程并生成工程产物。**

> **核心理念：AI shouldn't remember conversations. AI should remember projects.**
>
> PBDD 的目标不是让 AI 记住一次次对话，而是让项目自己拥有可读取、可演进、可验证的长期记忆。

PBDD 不定位为代码框架。它更接近 Kubernetes、Dockerfile、OpenAPI 或 MCP 这类工程规范：定义协议、状态、约定和产物边界，由不同 Runtime 或 Agent 实现。

## 核心定位

PBDD 由四个核心部分组成：

```text
PBDD
  ├── Protocol   # 协议：事件、生命周期、工作流、产物契约
  ├── Brain      # 项目大脑：项目状态数据库
  ├── Workflow   # 工程流程：状态转换规则
  └── Artifacts  # 工程产物：Spec、ADR、Task、Review、Release 等
```

一句话：

```text
Event -> Brain -> Workflow -> Artifacts
```

用户提出意图，Runtime 将其解释为事件；事件驱动工作流状态转换；Brain 记录项目状态；Artifacts 承载可交付的工程产物。

## 为什么不是框架

传统框架通常把业务代码组织方式、运行时依赖和扩展点绑定在一起。PBDD 不是这样。

PBDD 只定义：

- 项目清单：`pbdd.yaml`
- 项目状态模型：Brain
- 事件协议：Event
- 生命周期协议：Lifecycle
- 工作流状态机：Workflow
- 工程产物契约：Artifact
- 项目目录约定：Convention

PBDD 不定义：

- 具体 Agent 提示词
- IDE 插件行为
- 业务代码结构
- 某一种语言或框架
- 某一家 AI 平台的专有能力

## 仓库结构

当前工作区拆成三个可独立维护的项目：

```text
PBDD/
  ├── pbdd-spec/      # 规范：规则源
  ├── pbdd-skill/     # Runtime：Agent 实现
  └── pbdd-starter/   # Starter：项目模板
```

### `pbdd-spec/`

PBDD 的规范源。

它定义：

- Event 类型
- Brain 数据模型
- Workflow 生命周期
- Artifact Schema
- Project Manifest：`pbdd.yaml`
- Conformance 规则

规范必须保持机器可读优先。`schemas/` 和 `workflow/` 是约束来源，Markdown 文档用于解释意图。

### `pbdd-skill/`

PBDD 的 Agent Runtime 实现。

它负责：

- 读取 `pbdd.yaml`
- 加载 PBDD Spec
- 读取和维护 Brain
- 执行 Workflow 状态转换
- 创建或更新 Artifacts
- 面向不同 Agent 或 IDE 提供适配层

Runtime 可以包含提示词、脚本、适配器和测试，但不能重新定义规范。

### `pbdd-starter/`

PBDD 项目模板。

它只包含一个真实项目需要的最小结构：

```text
project/
  pbdd.yaml
  brain/
  artifacts/
  src/
  tests/
```

Starter 是规范的消费者，不包含 Protocol 或 Workflow 定义。

## 依赖方向

```text
pbdd-spec
  -> pbdd-skill
  -> pbdd-starter
  -> user project
```

依赖方向不能反过来。

- Spec 不依赖 Skill。
- Skill 实现 Spec。
- Starter 使用 Spec 和 Skill。
- 用户项目复制 Starter 并积累自己的 Brain 和 Artifacts。

## Brain 是什么

Brain 不是普通文档，而是项目状态。

推荐结构：

```text
brain/
  project.md
  feature/
  task/
  risk/
  decision/
  knowledge/
  timeline/
  health/
```

示例：

```text
Feature: Coupon
Status: Implementing
Owner: Agent
Progress: 60%
Tasks: TASK-22, TASK-23
```

Markdown 只是当前存储格式。语义上，Brain 是 Project Database。

## Workflow 是什么

Workflow 是状态转换，不是 Prompt。

例如 Feature 生命周期：

```text
Draft -> Planning -> Implementing -> Testing -> Done
```

所有 Agent 都应遵守同一套状态机。Runtime 的职责是读取 Workflow 定义并执行合法转换。

## Artifacts 是什么

Artifacts 是工程产物，不是 Brain。

常见产物包括：

- Spec
- ADR
- Task
- Review
- Release note
- Knowledge note
- Test evidence
- Code

Brain 记录当前状态和索引；Artifacts 保存可审阅、可交付、可追溯的工程内容。

## 快速开始

复制 Starter：

```powershell
Copy-Item -Recurse pbdd-starter my-project
```

进入项目：

```powershell
Set-Location my-project
```

编辑：

```text
pbdd.yaml
brain/project.md
```

然后让支持 PBDD 的 Agent Runtime 读取项目：

```text
Use PBDD to inspect the project manifest, update brain state, run the appropriate workflow, and maintain engineering artifacts.
```

## 当前版本

当前规范草案版本：

```text
0.1.0
```

当前状态：

- `pbdd-spec/`：初始规范草案
- `pbdd-skill/`：Codex Skill Runtime 初版
- `pbdd-starter/`：最小项目模板

## 提交规范

本仓库使用 Conventional Commits。

常用类型：

- `feat`: 新增能力
- `fix`: 修复问题
- `docs`: 文档更新
- `refactor`: 不改变行为的结构调整
- `chore`: 仓库维护、配置、杂项
- `test`: 测试相关
- `ci`: 自动化和 CI 配置

详细说明见 [docs/commit-convention.md](docs/commit-convention.md)。

## 设计原则

- Spec 是规则源，Runtime 是实现，Project 是消费者。
- 机器可读规范优先，Markdown 负责解释。
- Brain 维护状态，Artifacts 承载产物。
- Prompt 不属于协议核心。
- PBDD 不绑定任何 Agent、IDE、语言或平台。

## License

当前尚未声明 License。
