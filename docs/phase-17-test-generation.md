# Phase 17 - Test Generation

## Objective

Add the ability for AdityaCLI to generate pytest unit tests from existing source files.

This phase extends AdityaCLI from code understanding and review into code generation.

---

## Motivation

After implementing:

* File Explanation
* Project Awareness
* Code Review

the next logical step is helping developers write tests.

A coding assistant should be capable of:

* Understanding source code
* Identifying functions
* Generating test cases
* Producing pytest boilerplate

without manual intervention.

---

## Features Added

### Test Generation Prompt

Added:

```text
prompts/generate_tests.txt
```

Purpose:

Guide the model to behave as a Python testing engineer and generate pytest-based tests.

Rules:

* Use pytest
* Return only code
* Cover major functions
* Include edge cases where appropriate
* Avoid explanations

---

### Test Generation Command

Added:

```bash
python src/cli.py test <file_path>
```

Example:

```bash
python src/cli.py test src/session.py
```

---

### Source File Loading

Implemented functionality to:

```text
Read Source File
↓
Send File Contents To LLM
↓
Generate Tests
↓
Display Output
```

---

## Architecture

### User Flow

```text
User
↓
test command
↓
Load test prompt
↓
Load source file
↓
Build messages
↓
Call LLM
↓
Display generated tests
```

---

### Components

#### cli.py

Responsibilities:

* Register test command
* Build prompt payload
* Call LLM
* Display generated tests

---

#### test_generator.py

Responsibilities:

* Read source file contents

---

#### generate_tests.txt

Responsibilities:

* Define test generation behavior
* Enforce pytest output style

---

## Example Usage

```bash
python src/cli.py test src/session.py
```

Output:

```python
def test_save_session():
    ...

def test_load_session():
    ...
```

---

## Observations

The model successfully:

* Parsed source code
* Identified available functions
* Generated pytest structure
* Proposed relevant test cases

The generated tests were useful but not production-ready.

Some outputs contained:

* Missing imports
* Incorrect mocking syntax
* Assumptions about implementation details

Therefore:

```text
Generated Tests
=
Draft Tests

NOT

Guaranteed Executable Tests
```

Human verification remains necessary.

---

## Lessons Learned

### 1. Test Generation Is More Complex Than Review

Reviews produce suggestions.

Tests require executable code.

This increases the likelihood of hallucinations.

---

### 2. Small Models Can Produce Useful Boilerplate

Qwen 3.5 9B generated meaningful test structures despite limited compute resources.

This validates the project's goal of building useful developer tooling around local models.

---

### 3. Generated Code Requires Validation

The model can assist test creation.

The developer remains responsible for:

* Running tests
* Fixing failures
* Verifying correctness

---

## Phase Outcome

Successfully added automated test generation capability.

AdityaCLI can now:

* Explain files
* Understand projects
* Review code
* Generate pytest tests

This moves the project closer to future phases involving:

* Diff generation
* File creation
* File modification
* Automated refactoring

---


