import json
from typing import Any
from src.tools.base import ToolProtocol

class ToolRegistry:
    """Реестр инструментов, доступных агенту"""

    def __init__(self):
        self._tools: dict[str, ToolProtocol] = {}

    def register(self, tool: ToolProtocol) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> ToolProtocol | None:
        return self._tools.get(name)

    def get_all_specs(self) -> list[dict[str, Any]]:
        return [tool.openai_spec for tool in self._tools.values()]

    def execute(self, name: str, **kwargs) -> str:
        tool = self.get(name)
        if tool is None:
            return json.dumps({"error": f"Tool '{name}' not found"})
        return tool.execute(**kwargs)