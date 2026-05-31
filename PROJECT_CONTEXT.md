# AdityaCLI - Master Project Context

## Vision

AdityaCLI is a local-first AI developer assistant designed for small local models running on consumer hardware.

The goal is NOT to compete with Claude Code, OpenCode, OpenClaw, or Codex.

The goal is to:

1. Build a powerful local coding assistant.
2. Learn the architecture behind modern AI developer tools.
3. Optimize for small models, limited VRAM, and limited context.
4. Keep the human in control rather than building a fully autonomous agent.

---

# Core Philosophy

AdityaCLI should be:

* Local-first
* Tool-driven
* Human-controlled
* Model-agnostic
* Context-efficient

AdityaCLI should NOT:

* Depend on a specific model
* Depend on a specific vendor
* Require large GPUs
* Depend on huge context windows
* Rely on long autonomous agent loops

---

# Hardware Constraints

Current Hardware:

* 8 GB VRAM
* Local LM Studio
* 16k Context
* Qwen 3.5 9B

Design decisions should assume these constraints.

---

# Long-Term Architecture

User
↓
AdityaCLI
↓
Memory Layer
↓
Tool Layer
↓
Model Layer
↓
Provider

---

# Future Model Strategy

Different models should be usable for different tasks.

Examples:

Coding:

* Qwen 3.5 9B

Summarization:

* Gemma 4 2B

Vision:

* Gemma Vision

Advanced Reasoning:

* Claude
* GPT

AdityaCLI should eventually support model routing and provider switching.

---

# Memory Strategy

Long-Term Storage:

* Database

Active Context:

* UCM (Unified Context Memory)

UCM should contain:

* Project Summary
* Active Goals
* Important Decisions
* Open Tasks
* Loaded Memories

The database stores everything.

UCM stores only what the model needs right now.

---

# Development Roadmap

## Phase 1-15 (Completed)

Phase 1

* LM Studio integration

Phase 2

* Basic chat

Phase 3

* Streaming responses

Phase 4

* System prompts

Phase 5

* Session persistence

Phase 6

* Session loading

Phase 7

* Session deletion

Phase 8

* Conversation history

Phase 9

* Refactoring foundations

Phase 10

* Modular architecture

Phase 11

* UI abstraction

Phase 12

* Rich terminal UI

Phase 13

* Typer CLI foundation

Phase 14

* File explanation

Phase 15

* Project awareness

---

## Phase 16

Code Review

Goal:
Review files and suggest improvements.

---

## Phase 17

Test Generation

Goal:
Generate tests for source files.

---

## Phase 18

Diff Generation

Goal:
Show proposed modifications before applying.

---

## Phase 19

File Writing

Goal:
Create files from prompts.

---

## Phase 20

File Editing

Goal:
Modify existing files.

LinkedIn Milestone #2.

---

## Phase 21

Tool Registry

Goal:
Unified tool execution architecture.

---

## Phase 22

Web Search Tool

Goal:
Allow internet-assisted tasks.

---

## Phase 23

Terminal Command Tool

Goal:
Run controlled shell commands.

---

## Phase 24

Git Tool

Goal:
Git status, diff, commit, branch.

---

## Phase 25

UCM Foundation

Goal:
Unified Context Memory architecture.

---

## Phase 26

Memory Database

Goal:
Store project memories and summaries.

---

## Phase 27

Memory Loading

Goal:
Load selected memories into UCM.

---

## Phase 28

Intent Detection

Goal:
Determine user intent automatically.

---

## Phase 29

Natural Language Tool Calling

Goal:
Use tools directly from chat.

Example:
"Review src/main.py"

---

## Phase 30

Simple Agent Loop

Goal:
Tool → Result → Continue workflow.

---

## Phase 31

Provider Abstraction

Goal:
Support multiple AI providers.

---

## Phase 32

Provider Switching

Goal:
Switch models dynamically.

---

## Phase 33

Project Refactoring

Goal:
Move code across files automatically.

---

## Phase 34

Project Planning

Goal:
Generate implementation plans.

---

## Phase 35

Context Builder

Goal:
Automatically select relevant files.

---

## Phase 36

Repository Indexing

Goal:
Build project understanding database.

---

## Phase 37

Codebase Memory

Goal:
Persistent repository knowledge.

---

## Phase 38

Task Execution Engine

Goal:
Multi-step deterministic workflows.

---

## Phase 39

Workspace Awareness

Goal:
Understand entire workspace structure.

---

## Phase 40

AdityaCLI v1 Release

Goal:
Stable, usable local developer assistant.

---

# Success Criteria

AdityaCLI succeeds if:

* It can assist coding locally.
* It works well on consumer hardware.
* It reduces dependency on paid coding assistants.
* It teaches the architecture behind AI developer tools.
* Improvements are limited by model capability rather than missing engineering infrastructure.

---

# Long-Term Differentiator

Most systems solve limitations with:

* Bigger models
* Bigger context
* More compute

AdityaCLI aims to solve limitations with:

* Better memory
* Better context selection
* Better tooling
* Better architecture
