# Phase 08 — Conversation Memory

## Goal

Allow AdityaCLI to remember previous messages within a session.

## Problem

Before this phase, every request was independent.

Only the current user message was sent to the model.

As a result, the assistant could not remember information shared earlier in the conversation.

Example:

User: My name is Aditya

Assistant: Nice to meet you.

User: What is my name?

Assistant: I don't know.

## Solution

Introduce conversation history.

A list was created to store all user and assistant messages exchanged during the session.

Each message is stored with:

* role
* content

Example:

[
{
"role": "user",
"content": "My name is Aditya"
},
{
"role": "assistant",
"content": "Nice to meet you."
}
]

## Implementation

The application now:

1. Stores user messages
2. Stores assistant responses
3. Sends the entire conversation history with each request

Workflow:

System Prompt
↓
Conversation History
↓
Current Context
↓
Model Response

## Benefits

* Multi-turn conversations
* Context retention
* More natural interactions
* Foundation for persistent chat sessions

## Lessons Learned

* LLMs are stateless by default.
* Conversation memory must be managed by the application.
* Context is recreated by resending message history.
* Stateful applications require explicit memory management.

## Outcome

AdityaCLI can now remember information shared earlier in the same session and respond using previous conversation context.
