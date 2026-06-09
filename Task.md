# Current Task

## Goal

Transform AdityaCLI from a session-based memory system into a local-first AI Knowledge Operating System.

---

# Current Architecture Decisions

## Global Memory

* Explicitly saved only.
* Use `/save`.
* Never automatically extracted.
* Shared across all projects and chats.
* Accessed via `/use-global-memory`.

---

## Projects

Projects are top-level containers.

Examples:

* AdityaCLI
* GSoC
* Krayon

Each project contains:

* Project Memory
* Multiple Chats

---

## Project Memory

When creating a project:

* User provides:

  * Description
  * Goals
  * Constraints
  * Relevant context

Properties:

* Available automatically to chats inside that project.
* Isolated from other projects.
* Can be promoted to Global Memory using `/save`.

---

## Chats

Chats are independent context windows.

Two types:

### Project Chats

Belong inside projects.

Example:

AdityaCLI

* Frontend
* Backend
* Retrieval Engine

### Standalone Chats

Independent chats not belonging to projects.

Example:

* Resume Help
* Career Planning
* Random Discussion

---

## Chat Rules

* Multiple chats can remain active simultaneously.
* Each chat maintains its own context window.
* Chats never share context automatically.
* Chats become searchable knowledge bases after synchronization.

---

## Chat Synchronization

Commands:

* `/sync-chat`
* `/exit`

Behavior:

* Current conversation is processed.
* Knowledge database is updated.
* Progress is displayed to the user.

Example:

Syncing conversation...

Chunking messages...
Updating database...
Refreshing search index...

✓ Sync completed

Properties:

* Similar to `git commit`.
* Manual only.
* No automatic synchronization.

---

## Retrieval Modes

### Temporary Retrieval

Command:

`/use "chat name"`

Behavior:

* Searches specified chat database.
* Injects retrieved context for current message only.

---

### Persistent Retrieval

Command:

`/import "chat name"`

Behavior:

* Chat remains available throughout current active chat.
* Import state disappears when current chat exits.

Commands:

* `/unimport "chat name"`
* `/imports`

Properties:

* Non-transitive.
* Runtime only.
* Circular imports are allowed.

---

## MiniRAG Architecture

Active Chats:

* Use normal context windows.
* No retrieval.

Archived/Synchronized Chats:

* Converted into searchable databases.
* Retrieval performed using search.

Flow:

Active Chat
↓
/sync-chat
↓
Chunking
↓
SQLite + FTS5
↓
Searchable Knowledge Base

---

## Search Technology

Current implementation target:

* SQLite
* FTS5

Future enhancements:

* Embeddings
* Hybrid Retrieval

---

# Current Tasks

## Immediate

* [ ] Remove Memory V1/UCM integration.
* [ ] Finalize database entities.
* [ ] Design SQLite schema.
* [ ] Design retrieval engine architecture.
* [ ] Design synchronization pipeline.

---

## Chat Management

* [ ] Implement standalone chats.
* [ ] Implement project chats.
* [ ] Implement project memory.
* [ ] Implement chat naming.
* [ ] Implement `/list-chats`.
* [ ] Implement `/new`.

---

## Project Management

* [ ] Implement `/new-project`.
* [ ] Implement `/list-projects`.
* [ ] Implement project memory storage.
* [ ] Implement project selection.

---

## Retrieval Commands

* [ ] Implement `/use`.
* [ ] Implement `/import`.
* [ ] Implement `/unimport`.
* [ ] Implement `/imports`.
* [ ] Implement `/use-global-memory`.

---

## Global Memory

* [ ] Implement `/save`.
* [ ] Implement global memory search.
* [ ] Implement global memory listing.
* [ ] Implement memory deletion.

---

## Synchronization

* [ ] Implement `/sync-chat`.
* [ ] Implement `/exit` synchronization.
* [ ] Implement synchronization progress UI.
* [ ] Implement MiniRAG updates.

---

# Future Tasks

* Plugin system
* MCP compatibility
* LSP integration
* Embedding-based retrieval
* Hybrid search
* Extension ecosystem
