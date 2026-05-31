# Phase 16 - Code Review

## Objective

Add the ability for AdityaCLI to review source code files and provide feedback about:

* Purpose of the file
* Strengths
* Potential issues
* Code quality concerns
* Improvement suggestions

This is the first phase where AdityaCLI moves beyond understanding code and begins evaluating code.

---

## Motivation

Phase 14 introduced file explanation.

Phase 15 introduced project awareness.

The next logical step is code evaluation.

A coding assistant should not only explain code but also identify:

* Design issues
* Maintainability concerns
* Potential bugs
* Refactoring opportunities

---

## Features Added

### Review Prompt

Added:

```text
prompts/review_file.txt
```

Purpose:

Provide instructions that guide the model to act as a code reviewer rather than a code explainer.

---

### Review Command

Added:

```bash
python src/cli.py review <file_path>
```

Example:

```bash
python src/cli.py review src/main.py
```

---

### File Loading

Implemented file reading functionality.

Workflow:

```text
File
↓
Read Content
↓
Build Messages
↓
Send To LLM
↓
Display Review
```

---

## Architecture

### User Flow

```text
User
↓
review command
↓
Load review prompt
↓
Load target file
↓
Create messages
↓
Call LLM
↓
Display review
```

---

### Components

#### cli.py

Responsibilities:

* Register review command
* Build message payload
* Call LLM
* Display results

---

#### review.py

Responsibilities:

* Read file contents

---

#### review_file.txt

Responsibilities:

* Define review behavior
* Guide evaluation output format

---

## Example Usage

```bash
python src/cli.py review src/main.py
```

Output:

```text
Purpose

Strengths

Potential Issues

Suggestions
```

---

## Observations

The model successfully:

* Read source code
* Understood file purpose
* Generated structured reviews
* Identified some real improvement opportunities

The model also produced some generic or incorrect suggestions.

Therefore:

```text
Review Output
=
Suggestions

NOT

Ground Truth
```

Human verification remains necessary.

---

## Lessons Learned

### 1. Evaluation Is Harder Than Explanation

Explaining code is easier than reviewing code.

Reviews require:

* Reasoning
* Judgement
* Tradeoff analysis

which increases hallucination risk.

---

### 2. Small Models Can Still Be Useful

Qwen 3.5 9B produced useful feedback despite limited context and compute.

This supports the project's goal of building a capable local coding assistant on consumer hardware.

---

### 3. Architecture Reuse Works

The review feature reused:

* Existing prompt loading
* Existing LLM integration
* Existing CLI architecture

without major modifications.

This validates the modular design created in earlier phases.

---

## Phase Outcome

Successfully added code review capability to AdityaCLI.

AdityaCLI can now:

* Explain files
* Understand projects
* Review source code

This establishes the foundation for future phases involving:

* Test generation
* Diff generation
* File editing
* Automated refactoring

---