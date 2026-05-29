# Phase 07 — Streaming Responses

## Goal

Improve the user experience by displaying model output as it is generated instead of waiting for the entire response to complete.

## Problem

Before this phase, the application waited for the model to finish generating the entire response before displaying anything to the user.

Workflow:

User Message
↓
Model Generates Complete Response
↓
Application Receives Response
↓
Response Displayed

This created noticeable delays for longer outputs and made the application feel less interactive.

## Solution

Enable response streaming using the OpenAI-compatible API exposed by LM Studio.

Instead of waiting for the complete response, the model now sends small chunks of text as generation progresses.

Workflow:

User Message
↓
Model Generates Tokens
↓
Token Stream
↓
Application Prints Tokens Immediately
↓
Response Appears Gradually

## Implementation

The API request was modified to use:

stream=True

Instead of receiving a single response object, the application now receives a sequence of response chunks.

Each chunk contains a small piece of generated text.

The application processes these chunks in real time and prints them directly to the terminal.

## Key Discovery

During implementation, it was necessary to inspect the structure of streamed responses.

A streamed chunk contains generated text inside:

chunk.choices[0].delta.content

This differs from non-streaming responses, which use:

response.choices[0].message.content

Understanding this distinction was important for implementing streaming correctly.

## Benefits

* Faster perceived response times
* Improved user experience
* More natural interaction
* Similar behavior to modern AI tools

Examples:

* Claude Code
* Codex CLI
* Cursor
* Aider

## Lessons Learned

* Streaming and non-streaming responses use different response structures.
* AI applications often optimize for perceived latency rather than raw generation speed.
* Real-time output significantly improves usability for longer responses.
* Inspecting API objects is often necessary to understand undocumented behavior.

## Outcome

AdityaCLI now displays responses incrementally as they are generated, creating a more responsive and interactive terminal experience.
