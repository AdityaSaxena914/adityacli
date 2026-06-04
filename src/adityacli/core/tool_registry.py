from dataclasses import dataclass
from typing import Callable


@dataclass
class Tool:
    name: str
    description: str
    category: str
    handler: Callable

TOOLS = {}

def register_tool(tool: Tool):
    TOOLS[tool.name] = tool

def get_tool(name: str):
    return TOOLS.get(name)

def list_tools():
    return list(TOOLS.values())

def tool_exists(name: str):
    return name in TOOLS


def get_tools_by_category(category: str):
    return [
        tool
        for tool in TOOLS.values()
        if tool.category == category
    ]