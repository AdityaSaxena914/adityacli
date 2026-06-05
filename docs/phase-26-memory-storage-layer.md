# Phase 26 - Memory Storage Layer

## Goal

Create a persistent memory storage system independent of chat sessions.

The purpose of the Memory Storage Layer is to store important information that should survive across multiple conversations and sessions.

Examples:

* Architectural decisions
* Open tasks
* Session summaries
* Project knowledge

This information becomes the foundation for future retrieval systems.

---

## Problem

Session persistence allows conversations to continue.

However, important information remains trapped inside chat histories.

Examples:

Session 12:

* Use UCM architecture

Session 57:

* Add dependency-aware retrieval

Session 103:

* Implement repository intelligence

Without a dedicated memory system, AdityaCLI cannot easily access these decisions in future sessions.

---

## Solution

Introduce a dedicated Memory Database.

Memory Storage is separated from:

* Chat History
* Session Files
* Repository Knowledge

This creates a persistent project memory layer.

---

## Architecture

Long-Term Memory
↓
MemoryDB
↓
memory.json

Future Architecture:

MemoryDB
↓
Retriever
↓
UCM
↓
Model

---

## Implementation

Created:

```text
src/adityacli/memory/memory_db.py
```

Primary Class:

```python
class MemoryDB
```

---

## Storage Format

Current implementation uses JSON storage.

File:

```text
memory.json
```

Schema:

```json
{
    "decisions": [],
    "tasks": [],
    "summaries": [],
    "knowledge": []
}
```

---

## Memory Categories

### Decisions

Stores important architectural and project decisions.

Examples:

* Use model-agnostic memory
* Use local-first architecture
* Use dependency-aware retrieval

---

### Tasks

Stores active and pending tasks.

Examples:

* Implement retrieval engine
* Create repository indexer
* Improve terminal UI

---

### Summaries

Stores session summaries.

Purpose:

Provide compressed historical context without loading full conversations.

---

### Knowledge

Stores project knowledge and important information.

Examples:

* Repository insights
* Project rules
* Design constraints

---

## Core Functions

### load()

Loads memory data from disk.

Returns:

```python
dict
```

---

### save()

Writes memory data to disk.

Persists all changes.

---

### add_decision()

Adds a decision to memory storage.

---

### add_task()

Adds a task to memory storage.

---

### add_summary()

Adds a session summary to memory storage.

---

### add_knowledge()

Adds project knowledge to memory storage.

---

## Automatic Initialization

On first execution:

```text
MemoryDB
↓
memory.json not found
↓
Create memory.json
↓
Initialize schema
```

This ensures storage always exists before retrieval operations occur.

---

## Current Limitations

Current version:

* Uses JSON storage
* No retrieval engine
* No ranking system
* No semantic search
* No embeddings
* No automatic memory extraction

The objective of Phase 26 is persistence only.

---

## Result

AdityaCLI now has a dedicated long-term memory storage layer.

Memory can persist independently of chat sessions and will serve as the foundation for future retrieval, context assembly, and UCM integration systems.

Phase 26 establishes the storage layer required for building intelligent memory retrieval in later phases.
