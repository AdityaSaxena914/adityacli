# Phase 22 - Web Search Tool

## Goal

Add internet search capabilities to AdityaCLI.

This phase introduces web search functionality and search result summarization.

---

## Features Implemented

### Web Search

Created:

search.py

Implemented:

* search_web()
* DDGS integration
* Search result retrieval

---

### Search Command

Added:

adityacli search

Example:

adityacli search "python typing"

Returns:

* Title
* URL
* Description

for the top search results.

---

### Search Summarization

Added:

--summary

Example:

adityacli search "python typing" --summary

Workflow:

Search Query
↓
Web Search
↓
Result Collection
↓
LLM
↓
Summary

---

### Search Prompt

Created:

search_summary.txt

Purpose:

* Summarize search results
* Remove duplicate information
* Present key facts
* Avoid hallucinations

---

### Tool Registry Integration

Registered:

search

Category:

WEB

---

## Architecture

User
↓
search command
↓
DuckDuckGo Search
↓
Search Results
↓
Optional LLM Summary
↓
Output

---

## Commands

Raw Search:

adityacli search "query"

Summarized Search:

adityacli search "query" --summary

---

## Result

AdityaCLI can now retrieve real-time web information and optionally summarize it using the active language model.
