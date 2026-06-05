# Phase 27 - Memory Retrieval Engine

## Goal

Create a retrieval system capable of finding relevant memories from long-term storage.

The objective is to avoid loading all stored memories into context and instead retrieve only the most relevant information for the current task.

This establishes the foundation for future context assembly and UCM population.

---

## Problem

Phase 26 introduced persistent memory storage through MemoryDB.

However, stored memories alone provide no value if AdityaCLI cannot determine which memories are relevant to the current request.

Without retrieval:

MemoryDB
↓
All Memories
↓
Model

This becomes inefficient and wastes context.

---

## Solution

Introduce a dedicated retrieval layer.

The retrieval engine sits between MemoryDB and UCM.

Architecture:

MemoryDB
↓
Memory Retriever
↓
Relevant Memories
↓
UCM

---

## Implementation

Created:

```text
src/adityacli/memory/retrieval.py
```

Primary Class:

```python
class MemoryRetriever
```

The retriever receives a MemoryDB instance through dependency injection.

Example:

```python
db = MemoryDB()

retriever = MemoryRetriever(db)
```

This design allows future storage systems to be substituted without changing retrieval logic.

Examples:

* JSON MemoryDB
* SQLite MemoryDB
* Vector Database
* Hybrid Memory Store

---

## Retrieval Workflow

MemoryDB
↓
Load Memory Data
↓
Flatten Memory Categories
↓
Score Memories
↓
Filter Irrelevant Results
↓
Sort By Relevance
↓
Return Top Results

---

## Memory Flattening

MemoryDB stores information in separate categories:

```json
{
    "decisions": [],
    "tasks": [],
    "summaries": [],
    "knowledge": []
}
```

The retriever converts these categories into a unified searchable structure.

Example:

```python
[
    {
        "type": "decision",
        "content": "Use UCM architecture"
    },

    {
        "type": "task",
        "content": "Implement retrieval engine"
    }
]
```

This separates storage format from retrieval format.

---

## Retrieval Interface

Primary Method:

```python
retrieve(query, top_k=5)
```

Parameters:

* query
* top_k

Purpose:

Return the most relevant memories for a given query.

---

## Scoring System

Current Version:

Keyword Matching

Implementation:

```python
_score_memory()
```

Workflow:

Query
↓
Lowercase
↓
Tokenize
↓
Compare Words
↓
Generate Score

Example:

Query:

```text
ucm architecture
```

Memory:

```text
Use UCM architecture
```

Score:

```text
2
```

Matching Terms:

* ucm
* architecture

---

## Filtering

Memories with score:

```text
0
```

are removed.

Purpose:

Prevent irrelevant memories from entering context.

Example:

Before Filtering:

```text
Use UCM architecture
Use model agnostic memory
Implement retrieval engine
```

After Filtering:

```text
Use UCM architecture
```

---

## Ranking

Relevant memories are sorted by score.

Highest score appears first.

Example:

```text
Score 5
Score 3
Score 1
```

This ensures the most relevant memories are returned first.

---

## Top-K Retrieval

Only the highest-ranked memories are returned.

Example:

```python
retrieve(query, top_k=3)
```

Returns:

```text
Top 3 Results
```

Purpose:

Control context growth and preserve context window budget.

---

## Architectural Decisions

### Dependency Injection

Retriever receives MemoryDB through the constructor.

Reason:

Allow future storage implementations without changing retrieval logic.

---

### Dedicated Scoring Function

Relevance calculation is isolated inside:

```python
_score_memory()
```

Reason:

Future retrieval algorithms can replace the scoring system without modifying the rest of the pipeline.

Potential Future Implementations:

* BM25
* Embeddings
* Hybrid Retrieval
* LLM Re-ranking

---

## Current Limitations

Current implementation:

* Keyword-based
* No semantic understanding
* No embeddings
* No vector search
* No hybrid retrieval

This is intentional.

The goal of Phase 27 is to establish retrieval architecture, not final retrieval quality.

---

## Result

AdityaCLI can now:

* Load stored memories
* Search memory records
* Rank memory relevance
* Filter irrelevant memories
* Return top matching memories

Phase 27 establishes the retrieval layer required for context assembly and UCM population in future phases.

Workflow:

MemoryDB
↓
Retriever
↓
Relevant Memories

```
```
