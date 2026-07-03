# PBDD

中文 | [English](README.en.md)

## Project Brain Driven Development

```text
AI shouldn't remember conversations.
AI should remember projects.
```

给项目一个 Project Brain，让任何 AI Agent 变成持续维护项目的软件工程师。

<p align="center">
  <img src="docs/assets/pbdd-flow.svg" alt="PBDD turns requests into project memory and engineering workflow" width="820">
</p>

## 为什么是 PBDD？

今天的 AI 软件开发通常是这样：

```text
你
  -> "实现登录"
  -> AI 写代码
```

然后第二天：

```text
New Chat
  -> "继续"
  -> AI: "你能先解释一下这个项目吗？"
```

每一次对话都从零开始。

你的项目有记忆。

你的 AI 没有。

PBDD 要改变这一点：把长期记忆从聊天记录里拿出来，放回项目本身。

## The Shift

传统 AI 编程：

```text
Chat -> Context -> Code
```

PBDD：

```text
Event -> Project Brain -> Workflow -> Engineering -> Code
```

对话是临时的。

项目是长期的。

## How It Works

PBDD 把每一次用户请求都转成一个工程事件。

```text
User: 增加退款能力。

Agent:
  [1] 识别 Feature Event
  [2] 更新 Project Brain
  [3] 分析影响范围
  [4] 更新 Specification
  [5] 创建 Tasks
  [6] 实现功能
  [7] 测试变更
  [8] 回写 Brain
```

最终产物不只是代码，而是一个知道发生了什么、为什么变化、哪里还有风险、下一步该做什么的项目。

## Architecture

```text
                 User
                  |
                  v
            Project Agent
                  |
                  v
          PBDD Skill Runtime
                  |
                  v
             Project Brain
                  |
  ---------------------------------
  Workflow   Knowledge   State
  Spec       Tasks       History
  Risks      Decisions   Health
  ---------------------------------
                  |
                  v
              Source Code
```

PBDD 不是 Agent。

PBDD 是项目记忆和工程协议。任何 Agent 都可以遵守它。

## The Brain

```text
Project Brain
  |-- Features
  |-- Tasks
  |-- Knowledge
  |-- Architecture
  |-- Risks
  |-- Timeline
  |-- Decisions
  `-- Health
```

项目需要记住的一切，都应该在这里。

不在隐藏聊天记录里。

不在某个平台账号里。

不在某个 Agent 的私有上下文里。

## Demo First

给一个 Agent 一个 PBDD 项目，然后说：

```text
Add refund support.
```

一个理解 PBDD 的 Agent 应该知道工程动作：

```text
[ok] 创建 Feature Event
[ok] 更新 Project Brain
[ok] 分析受影响的规格和代码
[ok] 创建实现任务
[ok] 执行 Workflow
[ok] 测试变更
[ok] 记录决策、风险和进度
```

下一个 Agent 可以从项目继续，而不是从你的记忆继续。

## Principles

```text
一切从 Event 开始。

Project Brain 是事实源。

Agent 维护工程。

Human 维护业务意图。

Workflow over Prompt.

Projects over Conversations.
```

## Getting Started

```bash
git clone https://github.com/LittleBlacky/PBDD.git
cd PBDD
```

把 starter 复制成一个新项目：

```bash
cp -r pbdd-starter ../my-project
```

然后对你的 Agent 说：

```text
Boot this PBDD project.
```

这就是 PBDD 想提供的体验。

## Repository

```text
PBDD/
  pbdd-spec/      # 开放规范
  pbdd-skill/     # Agent Runtime 实现
  pbdd-starter/   # 项目模板
```

一个 PBDD 项目长这样：

```text
project/
  pbdd.yaml
  brain/
  artifacts/
  src/
  tests/
```

README 负责讲愿景。细节放在规范和文档里。

## Ecosystem

```text
PBDD Specification
        |
        v
PBDD Runtime / Skill
        |
        v
Agent
        |
        v
Project
```

PBDD 不应该属于某一个 AI 工具。

Claude、Cursor、ChatGPT、Codex、本地 Agent、CI Agent、未来的 IDE，都应该能遵守同一个 Project Brain。

## Roadmap

```text
[x] Project Brain
[x] Workflow model
[x] Event model
[x] Codex Skill runtime
[x] Starter project
[ ] Multi-agent workflow
[ ] Enterprise Brain
[ ] Cloud sync
[ ] IDE plugin
[ ] Visual workflow
[ ] Conformance test suite
```

## Manifesto

软件工程不是生成代码。

软件工程是演进项目。

PBDD 教 AI 如何演进软件。

项目应该拥有记忆。

Agent 应该拥有纪律。

工程应该走向自治。

```text
The future isn't AI writing code.
The future is AI owning software engineering.
```
