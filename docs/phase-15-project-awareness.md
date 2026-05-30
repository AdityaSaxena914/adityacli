# Phase 15 — Project Awareness

## Goal

Extend AdityaCLI from understanding individual source files to understanding an entire software project.

## Problem

The previous implementation could only analyze one file at a time.

While useful, software architecture is distributed across multiple files and modules.

Understanding a single file does not provide a complete view of a codebase.

## Solution

Introduce project awareness.

The assistant can now:

1. Discover source files.
2. Read multiple files.
3. Aggregate project context.
4. Analyze repository architecture.

## New Components

### get_project_files()

A new utility function was added.

Responsibilities:

* Traverse project directories.
* Locate Python files.
* Return file paths.

Implementation uses:

os.walk()

to recursively discover project files.

## Project Context Collection

All source files are collected into a single context.

Format:

FILE: src/main.py

<content>

FILE: src/chat.py

<content>

This allows the language model to reason about relationships between modules.

## New Prompt

project_explain.txt

Purpose:

Guide the model to perform repository-level analysis.

Focus areas:

* Project purpose
* Architecture
* Module responsibilities
* Data flow
* Improvements

## CLI Command

A new command was introduced:

python src/cli.py project

Workflow:

Project Command
↓
Discover Files
↓
Read Files
↓
Aggregate Context
↓
Load Project Prompt
↓
Qwen Analysis
↓
Repository Explanation

## Technical Flow

User
↓
project()
↓
get_project_files()
↓
read_file()
↓
load_prompt()
↓
get_completion()
↓
Qwen 3.5 9B
↓
Project Analysis

## Benefits

* Repository understanding
* Architecture analysis
* Cross-file reasoning
* Better developer assistance
* Foundation for future code intelligence features

## Lessons Learned

* Repository analysis is fundamentally different from file analysis.
* Context aggregation is necessary for architecture understanding.
* Reusable prompt templates simplify capability expansion.
* Modular utility functions accelerate development.

## Outcome

AdityaCLI can now analyze and explain the architecture of an entire codebase rather than a single source file.
