# Current Task

## Objective

Replace the UCM-based memory architecture (Memory V1) with a Workspace-Based Knowledge System (Memory V2).

Goal: Build a local-first, provider-agnostic knowledge system that works consistently across all models and sessions.

---

# Current Phase

Memory V2 Architecture Design

---

# Major Refactor Tasks

## 1. Remove Memory V1 Integration

* [ ] Remove UCM integration from chat flow
* [ ] Remove ContextBuilder usage
* [ ] Remove MemoryRetriever usage from runtime
* [ ] Remove MemoryExtractor usage from runtime
* [ ] Remove MemoryManager usage from runtime
* [ ] Archive old memory implementation as `memory_v1/`

---

## 2. Workspace System Design

* [ ] Replace Session concept with Workspace concept
* [ ] Define Workspace lifecycle
* [ ] Support workspace creation
* [ ] Support workspace switching
* [ ] Support workspace renaming
* [ ] Support listing all workspaces
* [ ] Support workspace metadata

Commands:

* `/workspace create`
* `/workspace switch`
* `/workspace rename`
* `/workspace list`
* `/workspace info`

---

## 3. Global Memory System

Global memory should persist across:

* Models
* Providers
* Workspaces
* Sessions

Implement:

* [ ] Save global memory
* [ ] List global memory
* [ ] Delete global memory
* [ ] Search global memory

Commands:

* `/save`
* `/memory`
* `/forget`

---

## 4. Workspace Knowledge System

Each workspace should support:

* [ ] Decisions
* [ ] Tasks
* [ ] Notes
* [ ] Summaries

Commands:

* `/decision`
* `/task`
* `/note`
* `/summary`

---

## 5. SQLite Migration

Replace JSON storage with SQLite.

Learn and implement:

* [ ] Tables
* [ ] Primary Keys
* [ ] Foreign Keys
* [ ] Indexes
* [ ] Transactions
* [ ] SQLite FTS5

Design database schema for:

* [ ] Workspaces
* [ ] Global Memories
* [ ] Tasks
* [ ] Decisions
* [ ] Notes
* [ ] Summaries
* [ ] Workspace Metadata

---

## 6. Retrieval System

Replace UCM with Retrieval Engine.

Implement retrieval flow:

User Query

↓

Current Workspace Search

↓

Mounted Workspace Search

↓

Global Memory Search

↓

Ranking

↓

Context Assembly

↓

LLM

Tasks:

* [ ] Current workspace retrieval
* [ ] Global memory retrieval
* [ ] Cross-workspace retrieval
* [ ] Result ranking
* [ ] Context builder

---

## 7. Workspace Mounting

Allow workspaces to access knowledge from other workspaces.

Features:

* [ ] Mount workspace
* [ ] Unmount workspace
* [ ] List mounted workspaces

Commands:

* `/mount`
* `/unmount`
* `/mounted`

Example:

Current Workspace: AdityaCLI

Mounted:

* GSoC
* Krayon

---

## 8. Search System

Implement knowledge search without loading everything into prompts.

Features:

* [ ] Full-text search
* [ ] Ranking
* [ ] Filter by workspace
* [ ] Filter by memory type

Commands:

* `/search`
* `/search-workspace`
* `/search-global`

---

## 9. Workspace Summarization

Reduce prompt size using summaries.

Features:

* [ ] Generate periodic summaries
* [ ] Store summaries
* [ ] Retrieve summaries during search

Strategies:

* Every N messages
* Manual summary generation

Commands:

* `/summarize`
* `/summaries`

---

## 10. Provider-Agnostic Design

Requirements:

* [ ] Works with LM Studio
* [ ] Works with OpenAI-compatible APIs
* [ ] Works with local models
* [ ] Shared knowledge across all providers
* [ ] Shared knowledge across all models

---

# Architecture Goals

* Local-first
* Offline-first
* Provider agnostic
* Model agnostic
* Explicit knowledge management
* Workspace-centric design
* Token efficient retrieval
* Scalable beyond JSON
* Production-quality architecture

---

# Learning Objectives

Required knowledge:

* [ ] SQLite
* [ ] Database design
* [ ] Full Text Search (FTS5)
* [ ] Retrieval systems
* [ ] Ranking systems
* [ ] Basic DBMS concepts

Future learning:

* [ ] Embeddings
* [ ] Vector databases
* [ ] Hybrid retrieval
* [ ] Advanced RAG

---

# Immediate Next Task

Design SQLite database schema for Memory V2.
