# Phase 25 - Unified Context Memory (UCM) Design

## Goal

Design the Unified Context Memory (UCM) architecture.

UCM acts as AdityaCLI's shared context layer and provides a unified view of relevant information regardless of which model is currently being used.

The objective is to create a model-agnostic context system that can be shared across local and cloud models.

---

## What UCM Is

UCM (Unified Context Memory) is the active context package used by AdityaCLI.

It is not a database.

It is not long-term memory.

It is not model-specific memory.

UCM exists to collect the most relevant information required for the current task and provide that information to any model.

Examples:

* Qwen
* GPT
* Claude
* Gemma

All models consume the same UCM.

---

## Design Principles

### Model Agnostic

Memory belongs to AdityaCLI.

Memory does not belong to any model.

Models may change.

UCM remains consistent.

---

### Context Focused

UCM stores only information relevant to the current task.

It should never contain the entire memory database.

It should never contain the entire repository.

---

### Shared Across Sessions

Information may originate from:

* Session 5
* Session 42
* Session 103

and appear together inside UCM if relevant to the current task.

---

### Single Source of Context

All future context assembly systems should target UCM.

Models receive context through UCM rather than directly from storage systems.

---

## Architecture

Current Session
↓
Context Extraction
↓
UCM

Long-Term Memory
↓
Retriever
↓
UCM

Repository Knowledge
↓
Repository Retrieval
↓
UCM

Tasks & Decisions
↓
Context Assembly
↓
UCM

UCM
↓
Prompt Builder
↓
Model

---

## Proposed UCM Schema

```python
{
    "active_goal": "",

    "current_task": "",

    "conversation_context": [],

    "retrieved_memories": [],

    "session_summaries": [],

    "important_decisions": [],

    "open_tasks": [],

    "repository_context": [],

    "metadata": {}
}
```

---

## Component Definitions

### Active Goal

Current high-level objective.

Example:

"Implement Memory Retrieval Engine"

---

### Current Task

Immediate task being worked on.

Example:

"Create retrieval ranking algorithm"

---

### Conversation Context

Relevant information from the active conversation.

---

### Retrieved Memories

Relevant memories loaded from long-term storage.

---

### Session Summaries

Relevant summaries from previous sessions.

---

### Important Decisions

Architectural or project decisions that should influence future work.

Examples:

* Local-first architecture
* Model-agnostic design
* Shared UCM ownership

---

### Open Tasks

Tasks currently in progress or pending.

---

### Repository Context

Relevant repository information loaded from indexing systems.

Examples:

* Related files
* Dependencies
* Symbols
* Repository knowledge

---

## Ownership Rules

UCM is owned by AdityaCLI.

Not by:

* GPT
* Claude
* Qwen
* Gemma

Models are consumers of UCM.

Models may contribute information that eventually becomes part of long-term memory.

---

## Data Flow

### Reading

Long-Term Memory
↓
Retriever
↓
UCM

Repository Index
↓
Retriever
↓
UCM

Current Session
↓
UCM

---

### Writing

Current Session
↓
Summarization
↓
Long-Term Memory

Important Decisions
↓
Long-Term Memory

Tasks
↓
Long-Term Memory

UCM itself is temporary and rebuilt when needed.

---

## What UCM Must Never Store

* Entire conversations
* Entire repositories
* Entire memory databases
* Raw embedding collections
* Irrelevant historical information

Only relevant context should be loaded.

---

## Long-Term Vision

UCM becomes the shared RAM of AdityaCLI.

Long-Term Memory acts as persistent storage.

Repository Knowledge acts as structured project storage.

Models become interchangeable consumers of the same context layer.

This architecture allows AdityaCLI to maintain consistent memory and context across multiple sessions, multiple providers, and multiple models.
