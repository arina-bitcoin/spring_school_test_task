from typing import Protocol, Any, Optional
from openai import OpenAI

class LLMClientProtocol(Protocol):
    """Контракт для языковой модели, умеющей работать с инструментами"""
    def create_completion(self, messages: list[dict[str, Any]], tools: Optional[list[dict]] = None) -> Any:
        ...

class OpenAICompatibleClient:
    """Клиент для OpenAI-совместимых API"""
    def __init__(self, client: OpenAI, model: str):
        self._client = client
        self.model = model

    def create_completion(self, messages, tools=None, temperature=0.2):
        kwargs = dict(
            model=self.model,
            messages=messages,
            temperature=temperature
        )
        if tools:
            kwargs["tools"] = tools
            kwargs["tool_choice"] = "auto"
        return self._client.chat.completions.create(**kwargs)