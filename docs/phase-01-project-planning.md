# Phase 01 — Project Planning

## Project Name

AdityaCLI

## Overview

AdityaCLI is a local-first terminal-based AI assistant powered by a locally running Qwen3.5 9B model through LM Studio's OpenAI-compatible API.

The project is inspired by tools such as Claude Code and Codex CLI, but intentionally starts with a much smaller scope to focus on understanding the underlying engineering concepts.

## Why I Am Building This

Most modern AI tools abstract away important concepts behind frameworks and managed services.

The goal of this project is to understand how AI-powered developer tools work internally by implementing the core components manually.

Key learning objectives:

* LLM integration
* Streaming responses
* Prompt engineering
* Context management
* Session persistence
* CLI application development
* Software architecture

## Project Goals

Version 1 should provide:

* Interactive terminal chat
* Streaming responses
* Conversation history within a session
* Configurable system prompts
* Local execution
* Clean architecture

## Non-Goals

Version 1 will not include:

* File editing
* Repository awareness
* Autonomous agents
* Tool calling
* RAG
* Multi-agent systems
* Cloud APIs

## Technology Stack

### Language

Python

### Model

Qwen3.5 9B

### Inference Engine

LM Studio

### Libraries

* OpenAI SDK
* Typer
* Rich
* Pydantic

## High-Level Architecture

User
↓
Terminal
↓
Typer CLI
↓
Chat Manager
↓
LM Studio API
↓
Qwen3.5 9B
↓
Streaming Response
↓
Terminal

## Future Roadmap

### Version 2

* Read files
* Explain files
* Summarize files

### Version 3

* Project awareness
* Repository scanning

### Version 4

* Tool execution
* Controlled file editing

### Version 5

* Local RAG

### Version 6

* Agent workflows

## Success Criteria

Version 1 is considered complete when:

* The user can launch the CLI
* Messages are sent to LM Studio
* Responses stream in real time
* Conversation history is maintained
* Markdown renders correctly in the terminal
* The codebase remains modular and maintainable
