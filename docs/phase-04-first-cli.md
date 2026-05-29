# Phase 04 — First Interactive CLI

## Goal

Transform the hardcoded API test into an interactive terminal application.

## Previous State

The previous implementation used a fixed prompt embedded in the source code.

Example:

"Hello, tell me who you are."

This verified API connectivity but was not interactive.

## Changes

Added terminal input using Python's built-in input() function.

The application now accepts prompts directly from the user and forwards them to the local model.

## Architecture

User
↓
Terminal Input
↓
OpenAI SDK
↓
LM Studio
↓
Qwen3.5 9B
↓
Response
↓
Terminal Output

## Result

Successfully created the first usable version of AdityaCLI.

Users can now ask arbitrary questions and receive responses from the local model.

## Lessons Learned

* Interactive applications require user input handling.
* Prompt content can be supplied dynamically at runtime.
* The OpenAI SDK integrates seamlessly with LM Studio's API.
* Small incremental milestones reduce debugging complexity.
