# Phase 24 - Git Tool

## Goal

Add repository awareness to AdityaCLI through Git integration.

This phase enables AdityaCLI to inspect repository status, history, branches, and file changes.

---

## Features Implemented

### Git Tool

Created:

git_tool.py

Implemented:

* git_status()
* git_diff()
* git_log()
* git_branch()

All Git operations reuse the existing terminal execution infrastructure from Phase 23.

---

### Repository Status

Added:

git-status

Example:

adityacli git-status

Purpose:

* Show modified files
* Show staged files
* Show untracked files
* Display repository state

---

### Repository Diff

Added:

git-diff

Example:

adityacli git-diff

Purpose:

* Show changes since the last commit
* Display added lines
* Display removed lines
* Inspect uncommitted work

---

### Commit History

Added:

git-log

Example:

adityacli git-log

Purpose:

* Display recent commits
* Show commit history
* Track repository progress

---

### Branch Information

Added:

git-branch

Example:

adityacli git-branch

Purpose:

* Display available branches
* Identify current branch

---

### Tool Registry Integration

Registered:

* git-status
* git-diff
* git-log
* git-branch

Category:

GIT

---

## Architecture

User
↓
Git Command
↓
git_tool.py
↓
run_command()
↓
Git CLI
↓
Output

---

## Commands

Repository Status:

adityacli git-status

Repository Changes:

adityacli git-diff

Commit History:

adityacli git-log

Branches:

adityacli git-branch

---

## Result

AdityaCLI now has repository awareness and can inspect Git state without leaving the CLI.

This provides the foundation for future repository intelligence, workflow automation, and AI-assisted development features.
