# Phase 10 — Codebase Refactor

## Goal

Improve maintainability by separating responsibilities into dedicated modules.

## Problem

As new features were added, main.py began accumulating multiple responsibilities:

* OpenAI client creation
* Prompt loading
* Session management
* Conversation handling
* Streaming logic
* Application startup flow

This made the file increasingly difficult to maintain and extend.

## Solution

Refactor the application into smaller modules with clear responsibilities.

## New Structure

src/

├── main.py

├── config.py

├── llm.py

├── chat.py

└── session.py

## Module Responsibilities

### config.py

Stores application configuration.

Examples:

* Model name
* API endpoint
* API key
* System prompt path

Also contains logic for loading the system prompt.

### llm.py

Responsible for creating and returning the OpenAI client.

This isolates model connection logic from the rest of the application.

### session.py

Handles conversation persistence.

Responsibilities:

* Save session
* Load session
* Delete session
* Check session existence

### chat.py

Handles communication with the language model.

Responsibilities:

* Send requests
* Stream responses
* Collect assistant output

### main.py

Acts as the application orchestrator.

Responsibilities:

* Startup flow
* Session selection
* User input loop
* Message construction
* History updates

## Benefits

* Cleaner architecture
* Better separation of concerns
* Easier debugging
* Easier feature development
* Reduced complexity in main.py

## Lessons Learned

* Refactoring is not adding features.
* Refactoring improves maintainability without changing behavior.
* Modular design simplifies future development.
* Clear ownership of responsibilities reduces coupling.

## Outcome

AdityaCLI now follows a modular architecture that can support future additions such as Rich UI, Typer commands, file operations, project awareness, and agent workflows.
