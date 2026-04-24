from typing import Protocol, Any, runtime_checkable

@runtime_checkable
class ToolProtocol(Protocol):
    """Контракт для любого инструмента агента"""

    @property
    def name(self) -> str:
        """Уникальное имя инструмента"""
        ...

    @property
    def description(self) -> str:
        """Человекочитаемое описание для LLM"""
        ...

    @property
    def parameters(self) -> dict[str, Any]:
        """JSON Schema для параметров функции"""
        ...

    def execute(self, **kwargs) -> str:
        """Выполнить инструмент и вернуть результат в виде JSON-строки"""
        ...

    @property
    def openai_spec(self) -> dict[str, Any]: ...


class ToolRegistryProtocol(Protocol):
    """Контракт для реестра инструментов"""

    def register(self, tool: ToolProtocol) -> None:
        """Зарегистрировать инструмент в реестре"""
        ...

    def get(self, name: str) -> ToolProtocol | None:
        """Получить инструмент по имени (или None, если не найден)"""
        ...

    def get_all_specs(self) -> list[dict[str, Any]]:
        """Вернуть список спецификаций всех инструментов для LLM"""
        ...

    def execute(self, name: str, **kwargs) -> str:
        """Выполнить инструмент по имени с переданными аргументами"""
        ...

