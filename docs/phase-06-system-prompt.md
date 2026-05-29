# Phase 06 — System Prompt Integration

## Goal

Give AdityaCLI a consistent identity and behavior across all user interactions.

## Problem

Before this phase, the application only sent the user's message to the model.

Example:

User Message
↓
Qwen3.5
↓
Response

As a result, the model responded according to its default training and identified itself as Qwen3.5.

Example:

User: What is your name?

Response:
"I am Qwen3.5..."

This behavior did not match the intended purpose of AdityaCLI.

## Solution

Introduce a system prompt.

A system prompt is a special instruction sent before the user's message. It defines the assistant's role, behavior, constraints, and personality.

The system prompt is stored in:

prompts/system.txt

and loaded at application startup.

## Implementation

The application now sends:

System Prompt
↓
User Message
↓
Qwen3.5
↓
Response

Example message structure:

[
{
"role": "system",
"content": system_prompt
},
{
"role": "user",
"content": user_prompt
}
]

## Why Store Prompts In A File

Instead of hardcoding instructions in Python:

* Easier maintenance
* Easier experimentation
* Cleaner separation of concerns
* Supports future prompt templates

This follows patterns commonly used in production AI systems.

## Results

Before:

User: What is your name?

Response:
"I am Qwen3.5"

After:

User: What is your name?

Response:
"I am AdityaCLI"

The assistant now follows project-specific instructions rather than relying entirely on its pretrained identity.

## Lessons Learned

* Model behavior is heavily influenced by prompts.
* System prompts are a core component of AI applications.
* Prompt engineering is part of application design.
* Separating prompts from code improves maintainability.

## Outcome

AdityaCLI now has a configurable identity and behavior layer, providing a foundation for future capabilities.
