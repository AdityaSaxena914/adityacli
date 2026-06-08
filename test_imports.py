from adityacli.memory.memory_db import MemoryDB
from adityacli.memory.retrieval import MemoryRetriever


db = MemoryDB()

# Clear existing memory.json for clean testing
db.save(
    {
        "decisions": [],
        "tasks": [],
        "summaries": [],
        "knowledge": []
    }
)

# Add structured memories
db.add_decision(
    {
        "description": "Use SQLite for long-term memory storage",
        "reasoning": "SQLite scales better than JSON files"
    }
)

db.add_task(
    {
        "description": "Implement repository indexing"
    }
)

db.add_knowledge(
    {
        "description": "AdityaCLI follows a local-first architecture"
    }
)

retriever = MemoryRetriever(db)

queries = [
    "SQLite",
    "JSON files",
    "repository",
    "local-first",
    "scales better",
    "nothing"
]

for query in queries:

    print("\n" + "=" * 50)
    print(f"QUERY: {query}")

    results = retriever.retrieve(query)

    if not results:
        print("No results found.")
        continue

    for result in results:
        print(f"\nScore: {result['score']}")
        print(f"Type: {result['memory']['type']}")
        print(f"Content: {result['memory']['content']}")

        if "metadata" in result["memory"]:
            print("Metadata:")
            print(result["memory"]["metadata"])