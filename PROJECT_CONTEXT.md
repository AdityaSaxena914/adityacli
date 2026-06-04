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
* Tool Registry
* Tool Metadata System
* Tool Discovery
* Tool Categories
* Web Search
* Search Result Summarization
* Terminal Command Execution
* Terminal Output Capture
* Git Status
* Git Diff
* Git Log
* Git Branch
* Git Tool Integration
* Project Documentation System
* Global CLI Installation

Current Command:

adityacli

Current Tool Categories:

* CORE
* ANALYSIS
* CODE
* FILE
* WEB
* SYSTEM
* GIT


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

Memory Retrieval Layer

↓

Unified Context Memory (UCM)

↓

Context Builder

↓

Model Layer

↓

Provider

Multiple models may consume the same UCM.

UCM acts as the shared context layer for AdityaCLI rather than belonging to any individual model.


---

# Memory Strategy

## Long-Term Memory

Persistent Storage contains:

* Session History
* Session Summaries
* Important Decisions
* Tasks
* Repository Knowledge
* Embeddings
* User Preferences
* Project Knowledge

Long-Term Memory is the permanent knowledge store of AdityaCLI.

Nothing is sent directly from Long-Term Memory to the model.

---

## Unified Context Memory (UCM)

UCM (Unified Context Memory) is AdityaCLI's model-agnostic shared context layer.

UCM is not a database.

UCM is not long-term storage.

UCM acts as the active context package for the current task.

Purpose:

* Aggregate relevant information from multiple sessions
* Aggregate retrieved memories
* Aggregate repository knowledge
* Aggregate active goals and tasks
* Provide a unified view of the current state

UCM may contain:

* Active Goal
* Project Summary
* Important Decisions
* Open Tasks
* Relevant Memories
* Relevant Session Summaries
* Relevant Repository Knowledge
* Current Conversation Context

UCM is shared across all models.

The memory belongs to AdityaCLI, not the model.

Examples:

* Qwen
* Claude
* GPT
* Gemma

can all consume the same UCM.

---

## Memory Flow

Current Session
↓
Session Summary
↓
Long-Term Memory

Long-Term Memory
↓
Retriever
↓
Context Assembly
↓
UCM
↓
Model(s)

Models may read from UCM and contribute new information back to Long-Term Memory through summaries, decisions, tasks, and knowledge extraction.

---

## Design Goal

The objective is not to give models larger context windows.

The objective is to provide the smallest possible context containing the highest-value information.

UCM acts as the shared RAM of AdityaCLI.

Long-Term Memory acts as the persistent storage layer.


---

# Development Roadmap

## Phase 25

Unified Context Memory (UCM) Architecture

Implement:

* UCM schema
* Context containers
* Session context support
* Memory context support
* Repository context support
* Task context support
* Decision context support
* Context serialization
* Context injection format

Goal:

Create a model-agnostic shared context layer capable of providing a unified view of relevant information regardless of which model is being used.

---

## Phase 26

Memory Storage Layer

Implement:

* SQLite storage
* Session records
* Session summaries
* Important decisions
* Task records
* Embedding storage
* Repository knowledge storage
* Metadata indexing

Goal:

Persistent long-term storage for all AdityaCLI knowledge.

---

## Phase 27

Memory Retrieval Engine

Implement:

* Similarity search
* Relevance ranking
* Session retrieval
* Decision retrieval
* Task retrieval
* Repository retrieval
* Context scoring

Goal:

Retrieve the most relevant information from long-term storage for the current task.

Workflow:

Memory Database
↓
Retriever
↓
Candidate Context

---

## Phase 28

Context Assembly Engine

Implement:

* Intent-aware retrieval
* Session summary loading
* Decision loading
* Task loading
* Repository knowledge loading
* Context ranking
* Context compression
* UCM population

Workflow:

Memory Database
↓
Retriever
↓
Context Assembly
↓
UCM
↓
Model

Goal:

Construct the smallest and most relevant UCM possible for each request.


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
* Dependency-aware context selection
* Function tracing
* Class tracing
* Import tracing
* Dependency tracing
* Context ranking
* Context compression
* Context budget management

Goal:

Build the smallest useful context possible for the model.

The system should understand relationships between files instead of retrieving files independently.

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
* Dependency graph generation
* Import graph generation
* Reverse dependency lookup
* File relationship analysis

Goal:

Navigate and understand large codebases efficiently.

This system becomes the foundation for repository intelligence and context building.

---

## Phase 36

Repository Indexing

Implement:

* AST parsing
* Function extraction
* Class extraction
* Module extraction
* Import extraction
* Symbol extraction
* Dependency extraction
* File metadata generation
* Symbol metadata generation
* Repository metadata generation
* Code chunking
* Embedding generation

Goal:

Build structured repository knowledge that can be queried efficiently.

Repository knowledge should contain both semantic information and structural relationships.

---

## Phase 36.5

Repository Q&A

Implement:

* Repository question answering
* Semantic retrieval
* Dependency-aware retrieval
* Relationship-aware retrieval
* Context generation
* Repository search
* Context expansion through imports
* Context expansion through references

Examples:

* Where is authentication implemented?
* How does session persistence work?
* Which module handles configuration?
* Which files depend on session.py?
* What would break if this function changes?

Goal:

Talk to codebases while understanding repository structure and dependencies instead of relying only on semantic search.

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
