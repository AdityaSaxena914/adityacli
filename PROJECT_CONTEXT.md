# AdityaCLI - Master Project Context

## Current Status

Completed:

* Chat
* Streaming Responses
* System Prompts
* Session Persistence
* Session Loading
* Session Deletion
* Conversation History
* Rich Terminal UI Foundation
* Typer CLI Architecture
* File Explanation
* Project Explanation
* Code Review
* Test Generation
* Diff Generation
* File Creation
* File Editing
* Approval Workflow
* Package Refactor
* Portable CLI Command

Current Command:

adityacli

---

# Vision

AdityaCLI is a local-first AI developer assistant optimized for small local models.

Primary goals:

* Maximize capability from small models.
* Minimize context usage.
* Keep the human in control.
* Build reusable AI tooling infrastructure.
* Support multiple models and providers.

---

# Design Principles

AdityaCLI should be:

* Local-first
* Model-agnostic
* Tool-driven
* Context-efficient
* Memory-centric
* Human-controlled

AdityaCLI should not depend on:

* Large context windows
* Large GPUs
* Vendor-specific APIs
* Autonomous long-running agents

---

# Hardware Assumptions

Current target hardware:

* 8GB VRAM
* Local LM Studio
* 16k Context Window

Future features should assume these constraints.

---

# Long-Term Architecture

User
↓
CLI Layer
↓
Intent Layer
↓
Tool Layer
↓
Memory Layer
↓
Context Builder
↓
Model Layer
↓
Provider

---

# Memory Strategy

Persistent Storage:

* Database
* Embeddings
* Repository Knowledge
* User Preferences

Active Memory:

UCM (Unified Context Memory)

UCM contains:

* Active Goals
* Project Summary
* Important Decisions
* Open Tasks
* Relevant Memories
* Relevant Repository Knowledge

Database stores everything.

UCM stores only what is needed for the current task.

---

# Development Roadmap

## Phase 21

Tool Registry

Implement:

* Tool registration
* Tool metadata
* Tool discovery
* Tool execution interface
* Tool categories

Goal:

Single architecture for all future tools.

---

## Phase 22

Web Search Tool

Implement:

* Search queries
* Result extraction
* Result summarization
* Search integration with chat

Goal:

Allow internet-assisted development tasks.

---

## Phase 23

Terminal Command Tool

Implement:

* Command execution
* Command output capture
* Safety restrictions
* Command validation

Goal:

Controlled shell access.

---

## Phase 24

Git Tool

Implement:

* git status
* git diff
* git commit
* git branch
* git log
* git blame

Goal:

Repository awareness.

---

## Phase 25

Unified Context Memory Foundation

Implement:

* UCM structure
* Context management
* Context insertion
* Context prioritization

Goal:

Control what information reaches the model.

---

## Phase 26

Memory Database

Implement:

* SQLite storage
* Embedding storage
* Vector search
* Memory records
* Repository knowledge records

Goal:

Persistent semantic memory.

---

## Phase 27

Memory Loading

Implement:

* Similarity search
* Relevance ranking
* Memory selection
* UCM population

Goal:

Load only useful memories.

---

## Phase 28

Intent Detection

Implement:

* Intent classification
* Tool recommendation
* Task categorization

Examples:

* Review
* Explain
* Edit
* Search
* Git
* Terminal

Goal:

Automatic workflow selection.

---

## Phase 29

Natural Language Tool Calling

Implement:

* Tool invocation from chat
* Parameter extraction
* Tool execution routing

Examples:

"Review session.py"

"Run pytest"

"Show git status"

Goal:

Use tools through conversation.

---

## Phase 30

Simple Agent Loop

Implement:

* Tool execution
* Observation
* Decision step
* Iteration control

Workflow:

Think
↓
Use Tool
↓
Observe
↓
Continue

Goal:

Multi-step task completion.

---

## Phase 31

Provider Abstraction

Implement:

* Provider interface
* Shared model API
* Configuration layer

Providers:

* LM Studio
* OpenAI
* Anthropic
* OpenRouter

Goal:

Provider independence.

---

## Phase 32

Provider Switching

Implement:

* Dynamic model selection
* Task routing
* Provider selection

Examples:

* Coding Model
* Summarization Model
* Vision Model

Goal:

Use the best model for each task.

---

## Phase 33

Project Refactoring

Implement:

* File movement
* Symbol movement
* Import updates
* Refactor validation

Additional Analysis:

* Dependency graph
* Import graph
* File relationships

Goal:

Safe automated refactoring.

---

## Phase 34

Project Planning

Implement:

* Feature planning
* Architecture planning
* Impact analysis
* Task breakdown

Goal:

Generate implementation plans before coding.

---

## Phase 35

Context Builder

Implement:

* Relevant file selection
* Dependency-aware context
* Function tracing
* Class tracing
* Import tracing
* Context ranking

Goal:

Build the smallest useful context.

This is a critical system.

---

## Phase 35.5

Code Intelligence Engine

Implement:

* Find symbol
* Find references
* Find implementation
* Find imports
* Find callers
* Find usages

Goal:

Navigate large codebases efficiently.

---

## Phase 36

Repository Indexing

Implement:

* AST parsing
* Function extraction
* Class extraction
* Module extraction
* Code chunking
* Embedding generation

Goal:

Build structured repository knowledge.

---

## Phase 36.5

Repository Q&A

Implement:

* Repository question answering
* Semantic retrieval
* Context generation
* Repository search

Examples:

* Where is authentication implemented?
* How does session persistence work?
* Which module handles configuration?

Goal:

Talk to codebases.

---

## Phase 37

Codebase Memory

Implement:

* Repository summaries
* Architectural summaries
* Component summaries
* Decision tracking

Goal:

Persistent repository understanding.

---

## Phase 38

Task Execution Engine

Implement:

* Plans
* Steps
* Progress tracking
* Execution state
* Rollback support

Goal:

Deterministic workflows.

---

## Phase 39

Workspace Awareness

Implement:

* Multi-project indexing
* Cross-project search
* Workspace graph
* Shared dependency analysis

Goal:

Understand the entire workspace.

---

## Phase 40

AdityaCLI v1

Requirements:

* Tool Registry
* Memory System
* Context Builder
* Repository Intelligence
* Multi-Provider Support
* Workspace Awareness

Goal:

Stable local developer assistant.

---

# Primary Differentiator

AdityaCLI should improve small-model performance through:

* Better Memory
* Better Context Selection
* Better Tooling
* Better Repository Intelligence
* Better Architecture

The objective is not bigger models.

The objective is making small models more effective.
