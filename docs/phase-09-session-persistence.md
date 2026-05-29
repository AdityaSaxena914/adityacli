# Phase 09 — Session Persistence

## Goal

Preserve conversation history across application restarts.

## Problem

Before this phase, conversation history existed only in memory.

Workflow:

Start Application
↓
Chat
↓
Exit
↓
Memory Cleared
↓
Conversation Lost

Although the assistant could remember previous messages during a session, all context was lost when the application closed.

## Solution

Implement session persistence using JSON storage.

Conversation history is now written to disk after each completed interaction and can be restored when the application starts again.

## Storage Format

File Location:

sessions/session.json

Data Format:

JSON

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

## Why JSON

The conversation history already exists as a Python list of dictionaries.

JSON provides a direct mapping to this structure.

Benefits:

* Human readable
* Easy debugging
* Native Python support
* Minimal implementation complexity

## Session Module

A dedicated module was created:

session.py

Responsibilities:

* Load session data
* Save session data
* Delete session data
* Check if a session exists

Functions:

load_session()

save_session(conversation_history)

delete_session()

session_exists()

## Resume Workflow

Application Startup
↓
Check for Existing Session
↓
Session Found?
├── No
│   ↓
│   Start New Session
│
└── Yes
↓
Ask User:
Resume previous session? (y/n)
│
├── y
│   ↓
│   Load Session
│
└── n
↓
Delete Session
↓
Start Fresh

## Save Strategy

The conversation is saved after every completed assistant response.

Workflow:

User Message
↓
Assistant Response
↓
Update History
↓
Save To Disk

This minimizes data loss if the application closes unexpectedly.

## Example

Session 1:

User:
"My name is Aditya"

Assistant:
"Nice to meet you."

Exit Application

Restart Application

Resume Session:
y

User:
"What is my name?"

Assistant:
"Your name is Aditya."

## Lessons Learned

* LLMs are stateless by default.
* Memory persistence must be implemented by the application.
* JSON is suitable for structured conversation data.
* Separating persistence logic into its own module improves maintainability.
* Saving state incrementally reduces risk of data loss.

## Outcome

AdityaCLI now supports persistent conversations across application restarts through automatic session storage and restoration.
