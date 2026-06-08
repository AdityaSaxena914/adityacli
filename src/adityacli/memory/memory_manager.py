from adityacli.memory.memory_db import MemoryDB
from adityacli.memory.memory_extractor import MemoryExtractor
from adityacli.memory.retrieval import MemoryRetriever

class MemoryManager:

    def __init__(
        self,
        db: MemoryDB,
        retriever: MemoryRetriever,
        extractor: MemoryExtractor
    ):

        self.db = db
        self.retriever = retriever
        self.extractor = extractor

    def process_conversation(
        self,
        user_message,
        assistant_message
    ):

        memories = self.extractor.extract(
            user_message,
            assistant_message
        )

        self._store_memories(
            memories["decisions"],
            "decision",
            self.db.add_decision
        )

        self._store_memories(
            memories["tasks"],
            "task",
            self.db.add_task
        )

        self._store_memories(
            memories["knowledge"],
            "knowledge",
            self.db.add_knowledge
        )

    def _store_memories(
        self,
        memories,
        memory_type,
        save_function
    ):

        for memory in memories:

            existing = self.retriever.retrieve(
                memory["description"],
                top_k=1
            )

            if not existing:

                save_function(memory)