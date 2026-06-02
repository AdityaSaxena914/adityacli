# Phase 20 - File Editing

## Objective

Enable AdityaCLI to modify existing files using LLM-generated changes while keeping the user in control through a diff and approval workflow.

This phase transforms AdityaCLI from a code analysis tool into a code modification tool.

---

## Motivation

Phase 19 introduced file creation.

However, creating new files is only a small part of software development.

A coding assistant must also be able to:

* Read existing code
* Understand requested modifications
* Generate updated code
* Show proposed changes
* Apply modifications safely

Phase 20 introduces this capability.

---

## Features Added

### File Editing Command

Added command:

```bash
python src/cli.py edit <file_path>
```

Example:

```bash
python src/cli.py edit src/session.py
```

---

### Edit Prompt

Added:

```text
prompts/edit_file.txt
```

Purpose:

* Understand modification requests
* Generate updated file content
* Return only code
* Prevent explanations and markdown formatting

---

### File Editor

Added:

```python
edit_file(file_path, updated_content)
```

Responsibilities:

* Receive updated content
* Overwrite target file
* Save modifications

Implementation:

```python
def edit_file(file_path, updated_content):
    write_file(file_path, updated_content)
```

---

## Workflow

### User Flow

```text
User
↓
edit command
↓
Read file
↓
Enter modification request
↓
Send file + request to LLM
↓
Generate updated file
↓
Generate diff
↓
Display diff
↓
User approval
↓
Apply changes
```

---

## Architecture

### cli.py

Responsibilities:

* Register edit command
* Read file content
* Accept modification request
* Build LLM prompt
* Generate diff
* Request approval
* Apply changes

---

### file_editor.py

Responsibilities:

* Save updated file content

---

### diff_generator.py

Responsibilities:

* Compare original file
* Compare modified file
* Display proposed changes

---

### edit_file.txt

Responsibilities:

* Guide modification behavior
* Restrict output to code only

---

## Safety Layer

Before modifying any file:

```text
Original File
↓
LLM Modification
↓
Diff Preview
↓
User Approval
↓
File Update
```

This prevents accidental overwrites.

---

## Validation

### Test Case

Command:

```bash
python src/cli.py edit src/session.py
```

Request:

```text
Add docstrings to all functions
```

Result:

```text
✓ File read successfully
✓ Updated content generated
✓ Diff displayed
✓ Approval requested
✓ Changes written to file
```

---

## Example Diff

```diff
def session_exists():
+    """Check whether a session file exists."""
     return os.path.exists("sessions/session.json")
```

---

## Why This Phase Matters

This phase introduces the core workflow used by modern coding assistants.

The system now supports:

```text
Read
↓
Understand
↓
Modify
↓
Review
↓
Apply
```

instead of simple analysis-only operations.

---

## Lessons Learned

### 1. Human Approval Is Critical

Direct file overwrites are unsafe.

A review stage significantly reduces risk.

---

### 2. Diff Generation Adds Transparency

Users can inspect:

* Added lines
* Removed lines
* Behavioral changes

before applying modifications.

---

### 3. Editing Is More Valuable Than Creation

Most real-world development involves modifying existing codebases rather than creating new files from scratch.

---

## Current AdityaCLI Capabilities

### Analysis

* Chat
* Session Persistence
* File Explanation
* Code Review
* Test Generation

### Modification

* Diff Generation
* File Creation
* File Editing

---

## Phase Outcome

Successfully implemented safe file editing.

AdityaCLI can now:

* Read existing source files
* Understand modification requests
* Generate updated code
* Display diffs
* Apply approved changes

using a local LLM.

---

## Commit

```bash
git commit -m "feat: add file editing with approval workflow"
```
