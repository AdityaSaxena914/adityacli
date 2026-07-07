# Fixes.md

**AdityaCLI V2 — Production Remediation & Engineering Specification**

**Last Updated:** Sunday, July 07, 2026

---

# Purpose

This document defines the mandatory engineering changes required to transform AdityaCLI from a prototype into a production-grade, local-first AI developer assistant.

It supersedes previous implementation decisions wherever necessary.

The objective is to improve:

* Security
* Reliability
* Maintainability
* Scalability
* Performance
* Extensibility

This document specifies **what must change**, **where it applies**, and **what technologies should be adopted**. It intentionally does **not** contain implementation code.

---

# 1. Remote Command Execution (RCE)

### Current Problem

`terminal_tool.py` executes commands through `subprocess.run(..., shell=True)`.

This exposes the application to command injection and unrestricted host execution.

### Required Changes

* Replace shell execution with `subprocess` using `shell=False`.
* Parse arguments safely using `shlex`.
* Restrict execution to the active workspace.
* Enforce execution timeout.
* Enforce CPU and memory limits.
* Require an explicit allowlist for permitted commands.
* Require user confirmation before executing destructive operations.
* Route commands outside the allowlist through Docker-based sandbox execution.

### Affected Module

* `terminal_tool.py`

### Technologies

* `subprocess`
* `shlex`
* `psutil`
* Docker SDK for Python

---

# 2. Workspace Security

### Current Problem

`file_utils.py` allows arbitrary filesystem access.

Path traversal (`../../`) and unrestricted file mutation are possible.

### Required Changes

* Define a workspace root.
* Resolve every requested path using `pathlib.Path.resolve()`.
* Reject every resolved path outside the workspace.
* Apply the same validation for reads, writes, edits, deletes and future MCP filesystem operations.

### Affected Module

* `file_utils.py`

### Technologies

* `pathlib`

---

# 3. Prompt Injection Protection

### Current Problem

External search results are injected directly into prompts.

Instruction-like content from websites may influence the model.

### Required Changes

* Wrap external content inside dedicated delimiters.

Example:

```text
<untrusted_search_content>
...
</untrusted_search_content>
```

* Update the system prompt to explicitly treat everything inside those blocks as inert data rather than executable instructions.

### Affected Module

* `search.py`

---

# 4. Database Migration

### Current Problem

State is stored inside JSON files.

Problems include:

* corruption
* rewrite overhead
* no transactions
* poor scalability

### Required Changes

Replace JSON persistence with SQLite.

Use:

* WAL mode
* ACID transactions
* normalized schema

Core entities:

* Projects
* Chats
* Messages

### Affected Modules

* `session.py`
* `memory_db.py`

### Technologies

* `sqlite3` (standard library)

---

# 5. Safe File Editing

### Current Problem

Generated edits overwrite source files directly.

A malformed response can permanently destroy files.

### Required Changes

* Write edits into a temporary file.
* Atomically replace the original using `os.replace()`.
* Keep a `.bak` backup before replacement.

### Affected Module

* `diff_generator.py`

---

# 6. Context Window Management

### Current Problem

Conversation history grows indefinitely.

Eventually exceeds the model context window.

### Required Changes

* Introduce deterministic token budgeting.
* Use a tokenizer compatible with the active local model.
* Define a hard context ceiling.
* Automatically summarize or remove the oldest messages before exceeding the limit.

### Affected Module

* `chat.py`

### Technologies

* Model-compatible tokenizer (verify compatibility before using `tiktoken`)

---

# 7. Remove Automatic Memory Extraction

### Current Problem

Every assistant response triggers automatic memory extraction.

This increases latency and token consumption.

### Required Changes

* Remove `memory_extractor.py`.
* Remove automatic extraction from the chat loop.
* Store memories only through explicit `/save`.

### Affected Module

* `memory_extractor.py`

---

# 8. Structured LLM Validation

### Current Problem

Structured model output is parsed directly with `json.loads()`.

Malformed output crashes the application.

### Required Changes

* Validate structured output using typed schemas.
* Reject invalid responses.
* Retry generation when validation fails.

### Affected Modules

* `memory_extractor.py`
* Tool execution pipeline

### Technologies

* `pydantic`
* `pydantic-settings`

---

# 9. Retrieval Engine

### Current Problem

Retrieval performs linear lexical scanning.

Poor relevance.

No ranking.

### Required Changes

Replace lexical retrieval with:

* SQLite FTS5
* native BM25 ranking
* relevance threshold
* duplicate filtering

### Affected Modules

* `retrieval.py`
* `context_builder.py`

### Technologies

* SQLite FTS5

---

# 10. Synchronization

### Current Problem

`/sync-chat` must remain the synchronization boundary.

### Required Changes

Retain manual synchronization.

Do **not** automatically persist every conversation turn.

The internal synchronization pipeline must execute inside one atomic SQLite transaction.

### Affected Modules

* Synchronization pipeline

---

# 11. Configuration

### Current Problem

Configuration values are hardcoded.

### Required Changes

Move all configuration to environment-driven settings.

Remove hardcoded:

* API keys
* endpoints
* model names

### Affected Module

* `config.py`

### Technologies

* `pydantic-settings`
* `python-dotenv`

---

# 12. Layered Architecture

### Current Problem

CLI and business logic are tightly coupled.

### Required Changes

Introduce:

* service layer
* repository layer
* dependency injection
* interface-based abstractions

### Technologies

* `abc`

---

# 13. Tool Registry

### Current Problem

The registry is globally mutable.

### Required Changes

* Replace module-level registration.
* Introduce explicit `register_all_tools()`.
* Standardize future tool execution around MCP.

### Affected Module

* `tool_registry.py`

### Technologies

* Official MCP Python SDK

---

# 14. Error Handling

### Current Problem

Errors are inconsistently handled.

Retries are missing.

### Required Changes

Introduce:

* retry policy
* exponential backoff
* typed exception hierarchy
* explicit error reporting

Example hierarchy:

* CLIError
* ToolError
* RetrievalError
* DatabaseError

### Technologies

* `tenacity`

---

# 15. Logging

### Current Problem

Application logging is minimal.

### Required Changes

Introduce structured logging.

Separate:

* application logs
* tool logs
* token stream logs

### Technologies

* `logging`
* `rich.logging`

---

# 16. Audit Logging & Token Accounting

### Current Problem

Tool execution and token usage are not recorded.

### Required Changes

Create dedicated SQLite tables for:

* tool execution
* timestamps
* actions
* targets
* token consumption
* chat statistics

---

# 17. Dependency Management

### Current Problem

Both `pyproject.toml` and `requirements.txt` exist.

### Required Changes

Use `pyproject.toml` as the single source of truth.

Deprecate `requirements.txt`.

---

# 18. Testing

### Current Problem

No production-quality automated tests.

### Required Changes

Introduce:

* unit tests
* integration tests
* regression tests
* coverage reporting

Developer tooling:

* Ruff
* Black
* MyPy
* pre-commit

### Technologies

* `pytest`
* `pytest-mock`
* `pytest-cov`
* `ruff`
* `black`
* `mypy`

---

# 19. Git Validation

### Current Problem

Git operations assume Git exists and the current directory is a repository.

### Required Changes

Verify:

* Git installation
* active repository

before executing Git commands.

### Affected Module

* `git_tool.py`

### Technologies

* `shutil.which()`
* `git rev-parse --is-inside-work-tree`

---

# 20. Chat Identity

### Current Problem

The application maintains one global session.

### Required Changes

Use the SQLite `chats` table.

Each chat must have its own persistent identity.

### Affected Module

* `session.py`

---

# 21. Remove UCM

### Current Problem

`ucm.py` is unused in the V2 architecture.

### Required Changes

Delete the UCM implementation completely.

---

# 22. Runtime UI

### Current Problem

Dashboard values are hardcoded.

### Required Changes

Read runtime configuration dynamically.

Display:

* current model
* backend
* endpoint

from live configuration.

### Affected Module

* `ui.py`

---

# 23. Workspace File Discovery

### Current Problem

Project scanning ignores `.gitignore`.

### Required Changes

Respect ignore rules during workspace traversal.

### Affected Module

* `file_utils.py`

### Technologies

* `pathspec`

---

# 24. File Encoding

### Current Problem

Only UTF-8 files are assumed.

### Required Changes

Introduce encoding fallback for unsupported files.

### Affected Module

* `file_utils.py`

### Technologies

* `chardet`

---

# 25. Diff Safety

### Current Problem

Large generated diffs are unrestricted.

### Required Changes

Introduce maximum size limits before generating or applying diffs.

### Affected Module

* `diff_generator.py`

---

# 26. Graceful Cancellation

### Current Problem

Ctrl+C interrupts execution abruptly.

### Required Changes

Implement graceful shutdown.

Stop streaming safely.

Persist partial state where appropriate.

### Affected Module

* `chat_session.py`

### Technologies

* `signal`

---

# 27. Command Sandboxing

### Current Problem

Allowlisted commands execute directly.

Everything else is unrestricted.

### Required Changes

Execute non-allowlisted commands inside isolated Docker containers.

Apply:

* CPU limits
* memory limits
* filesystem isolation
* optional network isolation

### Affected Module

* `terminal_tool.py`

### Technologies

* Docker SDK for Python

---

# 28. Project Token Budgeting

### Current Problem

The `project()` command loads entire projects without context budgeting.

### Required Changes

Apply the same tokenizer-driven budgeting strategy used by the chat system before constructing prompts.

### Affected Module

* `cli.py`

---

# Completion Criteria

AdityaCLI will be considered production-ready only after all items in this document have been implemented, tested, documented, and verified.
