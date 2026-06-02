# Phase 18 - Diff Generation

## Objective

Add the ability for AdityaCLI to generate and display code differences before applying any modifications.

This phase introduces a safety layer between code generation and file editing.

---

## Motivation

Previous phases allowed AdityaCLI to:

* Explain source files
* Review source files
* Generate tests

However, before implementing file modification features, the user must be able to inspect proposed changes.

Direct file editing without review is risky.

The solution is a diff generation system.

---

## Features Added

### Diff Command

Added command:

```bash
python src/cli.py diff <file_path>
```

Example:

```bash
python src/cli.py diff src/session.py
```

---

### Diff Prompt

Added:

```text
prompts/diff.txt
```

Purpose:

* Analyze source file
* Improve code quality
* Return only modified code
* Avoid explanations

---

### Diff Engine

Implemented:

```python
generate_diff(
    original_content,
    improved_content
)
```

using Python's built-in:

```python
difflib.unified_diff()
```

---

## Workflow

### User Flow

```text
User
↓
diff command
↓
Read source file
↓
Send source code to LLM
↓
Generate improved code
↓
Compare original vs improved
↓
Display unified diff
```

---

## Architecture

### Components

#### cli.py

Responsibilities:

* Register diff command
* Load file content
* Build LLM request
* Display generated diff

---

#### diff_generator.py

Responsibilities:

* Compare original code
* Compare improved code
* Generate unified diff output

---

#### diff.txt

Responsibilities:

* Guide LLM improvement behavior
* Restrict output to code only

---

## Example Output

```diff
- def session_exists():
-     return os.path.exists("sessions/session.json")

+ SESSION_PATH = "sessions/session.json"
+
+ def session_exists() -> bool:
+     return os.path.isfile(SESSION_PATH)
```

---

## Why This Phase Matters

This phase introduces the foundation for safe code modification.

Future phases will use this workflow:

```text
Generate Change
↓
Show Diff
↓
User Approval
↓
Apply Change
```

instead of:

```text
Generate Change
↓
Overwrite File
```

---

## Lessons Learned

### 1. LLM Suggestions Require Validation

The generated diff contained:

* Useful improvements
* Type hints
* Constant extraction

but also proposed behavior changes that may not be desirable.

Example:

* Introducing RuntimeError exceptions
* Adding console output

This confirms that generated code should be reviewed before application.

---

### 2. Diffs Are Better Than Raw Rewrites

Users can immediately see:

* Added lines
* Removed lines
* Behavioral changes

without modifying files.

---

### 3. Safety Before Automation

Diff generation creates a review stage that protects the codebase from unintended changes.

This becomes essential before implementing file writing and automatic editing.

---

## Phase Outcome

Successfully implemented code diff generation.

AdityaCLI can now:

* Explain files
* Review files
* Generate tests
* Generate code diffs

without modifying any source files.

---
