# Phase 19 - File Creation

## Objective

Enable AdityaCLI to generate new files using LLM output and save them directly to disk.

This is the first phase where AdityaCLI performs filesystem actions instead of only analyzing code.

---

## Motivation

Previous phases focused on:

* Chat
* Session Management
* File Explanation
* Code Review
* Test Generation
* Diff Generation

All of these were read-only operations.

Phase 19 introduces write capabilities.

---

## Features Added

### File Creation Command

Added command:

```bash
python src/cli.py create <file_path>
```

Example:

```bash
python src/cli.py create hello.py
```

---

### File Writer

Added:

```python
write_file(file_path, content)
```

Responsibilities:

* Create files
* Write generated content
* Save using UTF-8 encoding

Implementation:

```python
def write_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
```

---

### Create Prompt

Added:

```text
prompts/create_file.txt
```

Purpose:

* Generate complete code
* Return only code
* Prevent explanations
* Prevent markdown formatting

---

## Workflow

### User Flow

```text
User
↓
create command
↓
Enter request
↓
Send request to LLM
↓
Generate code
↓
Write file
↓
Save to disk
```

---

## Architecture

### cli.py

Responsibilities:

* Register create command
* Accept user request
* Build LLM messages
* Receive generated code
* Call file writer

---

### file_writer.py

Responsibilities:

* Create files
* Save generated content

---

### create_file.txt

Responsibilities:

* Control generation behavior
* Restrict output to code only

---

## Files Successfully Generated

Validation completed using:

### hello.py

Request:

```text
Create a Python script that prints Hello World
```

Result:

```python
print("Hello World")
```

---

### calculator.py

Request:

```text
Basic calculator with add, subtract, multiply and divide
```

Result:

* Generated successfully
* File created successfully

---

### todo.py

Request:

```text
Basic todo application
```

Result:

* Generated successfully
* File created successfully

---

## Lessons Learned

### 1. Prompt Quality Matters

An incorrect prompt configuration caused the model to generate:

* Explanations
* Markdown
* Usage instructions

instead of code-only output.

Fixing the prompt immediately improved output quality.

---

### 2. Writing Files Is Simple

The difficult part is not filesystem access.

The difficult part is generating correct content before writing.

---

### 3. Filesystem Actions Need Safety

This phase creates files directly.

Future phases will require:

* Validation
* Diff previews
* Approval workflows

before modifying existing code.

---

## Why This Phase Matters

This is the first transition from:

```text
AI Assistant
```

to:

```text
AI Assistant + Action
```

The model can now create real artifacts on disk.

---

## Phase Outcome

Successfully implemented file generation and file creation.

AdityaCLI can now:

* Explain files
* Review files
* Generate tests
* Generate diffs
* Create new files

using local LLMs.

---

## Commit

```bash
git commit -m "feat: add file creation"
```
