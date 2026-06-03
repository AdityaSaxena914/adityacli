# Phase 23 - Terminal Command Tool

## Goal

Add terminal command execution capabilities to AdityaCLI.

This phase allows AdityaCLI to execute shell commands and return their output directly to the user.

---

## Features Implemented

### Terminal Tool

Created:

terminal_tool.py

Implemented:

* run_command()

Responsibilities:

* Execute terminal commands
* Capture standard output
* Capture standard error
* Report execution status

---

### Command Execution

Implemented using:

subprocess.run()

Configuration:

* capture_output=True
* text=True
* shell=True

This allows AdityaCLI to execute commands and collect their results programmatically.

---

### Output Handling

Captured:

* stdout
* stderr
* returncode

Returned as structured data.

Example:

{
"success": True,
"stdout": "...",
"stderr": ""
}

---

### Terminal Command

Added:

adityacli terminal

Example:

adityacli terminal "dir"

Example:

adityacli terminal "python --version"

---

### Error Handling

Invalid commands are handled gracefully.

Example:

adityacli terminal "abcdefg"

Returns:

* Failure status
* Error message
* No application crash

---

### Tool Registry Integration

Registered:

terminal

Category:

SYSTEM

---

## Architecture

User
↓
Terminal Command
↓
run_command()
↓
subprocess.run()
↓
stdout / stderr
↓
Formatted Output

---

## Commands

Execute command:

adityacli terminal "command"

Examples:

adityacli terminal "dir"

adityacli terminal "python --version"

adityacli terminal "git status"

---

## Result

AdityaCLI can now interact directly with the local operating system and retrieve command output for future automation, tooling, and agent workflows.
