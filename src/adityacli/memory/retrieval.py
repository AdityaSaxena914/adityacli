from adityacli.memory.memory_db import MemoryDB


class MemoryRetriever:

    def __init__(self, db: MemoryDB):

        self.db = db
    
    
    def retrieve(self, query, top_k=5):
        data = self.db.load()
        memories = []

        for decision in data["decisions"]:
            memories.append(
                {
                    "type" : "decision",
                    "content" : (
                        decision["description"]
                        + " "
                        + decision.get("reasoning", "")
                    ),
                    "metadata": decision
                }
            )

        for task in data["tasks"]:
            memories.append(
                {
                    "type" : "task",
                    "content" : task["description"],
                    "metadata": task
                }
            )
        
        for summary in data["summaries"]:
            memories.append(
                {
                    "type" : "summary",
                    "content" : summary
                }
            )
        
        for knowledge in data["knowledge"]:
            memories.append(
                {
                    "type" : "knowledge",
                    "content" : knowledge["description"],
                    "metadata": knowledge
                }
            )

        scored_memories = []

        for memory in memories:
            score = self._score_memory(query, memory["content"])
            scored_memories.append(
                {
                    "memory": memory,
                    "score": score
                }
            )

        scored_memories = [
            memory
            for memory in scored_memories
                if memory["score"] > 0
        ]
        scored_memories.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return scored_memories[:top_k]

    def _score_memory(self, query, memory):

        query = query.lower()
        memory = memory.lower()

        query_words = query.split()
        memory_words = memory.split()

        score = 0

        for word in query_words:
            if word in memory_words:
                score += 1
        
        return score