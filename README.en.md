# PBDD

[中文](README.md) | English

## Project Brain Driven Development

```text
AI shouldn't remember conversations.
AI should remember projects.
```

Turn any AI Agent into a persistent software engineer by giving it a Project Brain.

<p align="center">
  <img src="docs/assets/pbdd-flow.svg" alt="PBDD turns requests into project memory and engineering workflow" width="820">
</p>

## Why PBDD?

Today, AI software development usually looks like this:

```text
You
  -> "Implement Login"
  -> AI writes code
```

Then tomorrow:

```text
New Chat
  -> "Continue"
  -> AI: "Can you explain your project?"
```

Every conversation starts from zero.

Your project has memory.

Your AI doesn't.

PBDD changes that. It moves durable memory out of chat history and into the project itself.

## The Shift

Traditional AI coding:

```text
Chat -> Context -> Code
```

PBDD:

```text
Event -> Project Brain -> Workflow -> Engineering -> Code
```

Conversations are temporary.

Projects are permanent.

## How It Works

The entry point is not a user-written process, and it is not a manual template copy. The entry point is the Skill.

A user enables the PBDD Skill inside an existing project and asks it to initialize PBDD. After that, the agent uses the Skill to create or read the Project Brain, load the spec, execute workflows, and keep the project maintained.

```text
User: Add refund support.

PBDD Skill:
  [1] Read pbdd.yaml. If missing, initialize PBDD
  [2] Create or load Project Brain
  [3] Detect Feature Event
  [4] Execute Workflow
  [5] Update Specs and Tasks
  [6] Drive the agent to implement code
  [7] Test the change
  [8] Update Project Brain
```

The result is not just code. The result is a project that knows what changed, why it changed, what remains risky, and what should happen next.

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

PBDD is not the agent. PBDD is the project memory and engineering protocol that any agent can follow.

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

Everything the project needs to remember lives here.

Not in a hidden chat.

Not in a vendor account.

Not in one agent's private context.

## Demo First

Give an agent a PBDD project and say:

```text
Add refund support.
```

A PBDD-aware agent should know the engineering move:

```text
[ok] Create a Feature Event
[ok] Update the Project Brain
[ok] Analyze affected specs and code
[ok] Create implementation tasks
[ok] Execute the workflow
[ok] Test the change
[ok] Record decisions, risks, and progress
```

The next agent can continue from the project, not from your memory.

## Principles

```text
Everything starts with an Event.

Project Brain is the source of truth.

Agents maintain engineering.

Humans maintain business intent.

Workflow over Prompt.

Projects over Conversations.
```

## Getting Started

First, enable the PBDD Skill in your agent environment.

Second, enter any existing project:

```bash
cd my-project
```

Third, tell your agent:

```text
Use the PBDD skill.
Initialize PBDD in this project.
```

The Skill creates the PBDD structure in the current project:

```text
pbdd.yaml
AGENTS.md
brain/
artifacts/
```

After that, the user should not manually maintain PBDD. The user states intent; the Skill tells the agent how to read the Project Brain, run workflows, update artifacts, and maintain project state.

## Repository

```text
PBDD/
  pbdd-spec/      # the open specification
  pbdd-skill/     # the agent runtime implementation
  pbdd-starter/   # the optional project template
```

After Skill initialization, a project looks like this:

```text
project/
  pbdd.yaml
  AGENTS.md
  brain/
  artifacts/
  src/
  tests/
```

The README is the vision. The details live in the spec and docs.

## Ecosystem

```text
PBDD Skill
     |
     v
Initialize Project Brain
     |
     v
Maintain Workflow
     |
     v
Evolve Project Continuously
```

PBDD should not belong to one AI tool.

The same project can be maintained by different agents. The key is to configure those agents with a PBDD Skill, so Claude, Cursor, ChatGPT, Codex, local agents, CI agents, and future IDEs can all follow the same Project Brain.

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

Software engineering is not about generating code.

It is about evolving projects.

PBDD teaches AI how to evolve software.

Projects should have memory.

Agents should have discipline.

Engineering should become autonomous.

```text
The future isn't AI writing code.
The future is AI owning software engineering.
```
