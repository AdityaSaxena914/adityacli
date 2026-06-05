import json
from pathlib import Path


class MemoryDB:

    def __init__(self):

        self.memory_file = Path("memory.json")

        if not self.memory_file.exists():
            self._initialize()


    def _initialize(self):

        data = {
            "decisions": [],
            "tasks": [],
            "summaries": [],
            "knowledge": []
        }

        with open(self.memory_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)


    def load(self):

        with open(self.memory_file, "r", encoding="utf-8") as file:
            return json.load(file)


    def save(self, data):

        with open(self.memory_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)


    def add_decision(self, decision):

        data = self.load()

        data["decisions"].append(decision)

        self.save(data)


    def add_task(self, task):

        data = self.load()

        data["tasks"].append(task)

        self.save(data)


    def add_summary(self, summary):

        data = self.load()

        data["summaries"].append(summary)

        self.save(data)


    def add_knowledge(self, knowledge):

        data = self.load()

        data["knowledge"].append(knowledge)

        self.save(data)