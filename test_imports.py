from src.adityacli.memory.memory_db import MemoryDB
from src.adityacli.memory.retrieval import MemoryRetriever


db = MemoryDB()

retriever = MemoryRetriever(db)

print(
    retriever.retrieve("ucm")
)