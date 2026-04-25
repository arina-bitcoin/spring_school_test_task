from openai import OpenAI

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