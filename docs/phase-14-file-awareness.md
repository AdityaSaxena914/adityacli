# Phase 14 — File Awareness

## Goal

Transform AdityaCLI from a conversational assistant into a coding assistant capable of understanding source code files.

## Problem

Until this phase, AdityaCLI could only answer questions based on user-provided text.

The assistant had no direct access to source code files and therefore could not analyze, explain, or reason about codebases.

Example:

User → Prompt

Assistant → Response

No file access existed.

## Solution

Introduce file awareness.

The application can now:

1. Accept a file path from the CLI.
2. Read the file from disk.
3. Send the file contents to the language model.
4. Generate an explanation of the code.

## New Components

### file_utils.py

A dedicated utility module was introduced for file operations.

Function:

read_file(file_path)

Responsibilities:

* Open file
* Read contents
* Return source code as text

### explain_file.txt

A dedicated prompt template was introduced.

Purpose:

Provide consistent instructions for source code explanations.

Focus areas:

* File purpose
* Architecture
* Control flow
* Important functions
* Potential improvements

This separates prompt engineering from application logic.

## CLI Integration

A new command was added:

python src/cli.py explain <file_path>

Example:

python src/cli.py explain src/main.py

Workflow:

CLI Command
↓
Read File
↓
Load Prompt Template
↓
Send to Qwen
↓
Generate Explanation

## Architecture Improvements

Prompt management was generalized.

Previous approach:

load_system_prompt()

New approach:

load_prompt(prompt_path)

Benefits:

* Reusable prompt loading
* Easier addition of new prompt types
* Cleaner architecture

Prompt paths are now maintained through configuration constants.

Examples:

* SYSTEM_PROMPT_PATH
* EXPLAIN_PROMPT_PATH

## Technical Flow

User
↓
Typer CLI
↓
explain()
↓
read_file()
↓
load_prompt()
↓
get_completion()
↓
Qwen 3.5 9B
↓
Explanation

## Benefits

* Source code understanding
* Foundation for repository analysis
* Reusable prompt architecture
* Reusable file utilities
* Expansion toward coding assistant capabilities

## Lessons Learned

* Tool capabilities should be implemented before agent behavior.
* Prompt templates should remain separate from business logic.
* File operations deserve dedicated utility modules.
* Small reusable abstractions simplify future features.

## Outcome

AdityaCLI can now analyze and explain source code files directly from the command line.

This is the first capability that moves the project beyond a generic chatbot and toward a practical AI coding assistant.
