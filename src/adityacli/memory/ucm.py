class UCM:
    """Unified Context Manager class to maintain and construct dynamic conversation contexts."""

    def __init__(self):
        self.active_goal = ""
        self.current_task = ""
        self.conversation_context = []
        self.retrieved_memories = []
        self.session_summaries = []
        self.important_decisions = []
        self.open_tasks = []
        self.repository_context = []
        self.metadata = {}

    def set_active_goal(self, goal):
        """Set the primary objective for the current session."""
        self.active_goal = goal

    def set_current_task(self, task):
        """Define the immediate action item to be executed."""
        self.current_task = task

    def add_decision(self, decision):
        """Record a significant choice made during execution."""
        self.important_decisions.append(decision)

    def add_task(self, task):
        """Append an open-ended or pending sub-task."""
        self.open_tasks.append(task)

    def add_memory(self, memory):
        """Store retrieved knowledge relevant to the current context."""
        self.retrieved_memories.append(memory)

    def add_repository_context(self, context):
        """Ingest external repository information into the active scope."""
        self.repository_context.append(context)

    def build_context(self):
        """Construct a formatted string representation of all contextual elements.
        
        Returns:
            str: A structured text block containing goals, tasks, decisions, memories, and context.
        """
        lines = []

        if self.active_goal:
            lines.append(f"ACTIVE GOAL\n{self.active_goal}\n")

        if self.current_task:
            lines.append(f"CURRENT TASK\n{self.current_task}\n")

        decision_lines = [f"- {d}" for d in self.important_decisions]
        if decision_lines:
            lines.extend(["IMPORTANT DECISIONS", *decision_lines])

        task_lines = [f"- {t}" for t in self.open_tasks]
        if task_lines:
            lines.extend(["OPEN TASKS", *task_lines])

        memory_lines = [f"- {m}" for m in self.retrieved_memories]
        if memory_lines:
            lines.extend(["MEMORIES", *memory_lines])

        context_items = []
        for item in self.repository_context:
            if isinstance(item, dict):
                content_str = "\n".join(f"{k}: {v}" for k, v in item.items())
                context_items.append(content_str)
            else:
                context_items.append(str(item))

        if context_items:
            lines.extend(["REPOSITORY CONTEXT", *context_items])

        return "\n".join(lines).strip()