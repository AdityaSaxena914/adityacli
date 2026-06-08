from adityacli.memory.ucm import UCM
from adityacli.memory.retrieval import MemoryRetriever

class ContextBuilder:
    def __init__(self, retriever: MemoryRetriever):
        self.retriever = retriever
        
    def build(self, query):

        ucm = UCM()
        memories = self.retriever.retrieve(
            query
        )
        for memory in memories:
            ucm.add_memory(
                memory["memory"]["content"]
            )
        return ucm