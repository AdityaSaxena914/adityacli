# Phase 24.5 - Project Refactor

Goal

Prepare AdityaCLI for upcoming memory, retrieval,
and tool-calling systems.

Changes

- Introduced core/
- Introduced tools/
- Introduced utils/
- Introduced ui/
- Introduced chat/

Moved Files

core/
- config.py
- llm.py
- session.py
- chat_session.py
- tool_registry.py

tools/
- search.py
- git_tool.py
- terminal_tool.py

utils/
- file_utils.py
- diff_generator.py

ui/
- ui.py

chat/
- chat.py

Benefits

- Better separation of concerns
- Easier scaling
- Cleaner imports
- Foundation for memory and repository systems

Result

Project structure is ready for UCM and future
architecture expansion.