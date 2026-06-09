# AdityaCLI

Local-first, provider-agnostic AI knowledge operating system for developers.

## Vision

AdityaCLI aims to provide a unified AI development environment that works across multiple models and providers while maintaining a shared knowledge base.

The system is designed to be:

* Local-first
* Offline-capable
* Provider agnostic
* Model agnostic
* Workspace-centric
* Retrieval-based
* Developer-focused

---

## Core Principles

### Provider Agnostic

Knowledge should remain independent of the underlying model.

The same knowledge base should work with:

* Local models (LM Studio, Ollama)
* OpenAI-compatible APIs
* Future model providers

Changing models should not affect stored knowledge.

---

### Workspace-Based Architecture

Knowledge is organized into workspaces rather than isolated chat sessions.

Examples:

* AdityaCLI
* GSoC
* Krayon Automation
* DSA

Each workspace maintains its own:

* Tasks
* Decisions
* Notes
* Summaries

---

### Global Knowledge

Permanent knowledge exists independently from workspaces.

Examples:

* Preferred technology stack
* Long-term goals
* Architectural preferences

Global knowledge is shared across all workspaces and models.

---

### Retrieval Over Context Dumping

AdityaCLI avoids injecting large amounts of historical context into prompts.

Instead, it:

1. Searches relevant knowledge sources
2. Retrieves the most relevant information
3. Builds minimal context for the model

This improves:

* Token efficiency
* Response quality
* Scalability

---

## Planned Features

### Workspace Management

* Create workspaces
* Switch workspaces
* Rename workspaces
* Mount workspaces
* Search workspaces

### Knowledge Management

* Global memory
* Workspace notes
* Decisions
* Tasks
* Summaries

### Retrieval Engine

* SQLite Full-Text Search (FTS5)
* Cross-workspace retrieval
* Global knowledge retrieval
* Context ranking

### Multi-Model Support

* Local models
* OpenAI-compatible APIs
* Shared knowledge across providers

---

## Current Status

Memory V1 (UCM-based architecture) has been completed and archived.

Development is currently focused on Memory V2:

Workspace-Based Knowledge System.

---

## Long-Term Goal

Transform AdityaCLI from a coding assistant into a local-first AI knowledge operating system for developers.
