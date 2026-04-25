from typing import Protocol, Any, Optional

class LLMClientProtocol(Protocol):
    """Контракт для языковой модели, умеющей работать с инструментами"""
    def create_completion(self, messages: list[dict[str, Any]], tools: Optional[list[dict]] = None) -> Any:
        ...