import json
from src.tools.base import ToolRegistryProtocol
from src.llm.base import LLMClientProtocol

class NewsAgent:
    SYSTEM_PROMPT = (
        "Ты новостной ассистент. Когда пользователь просит новости по любой теме, "
        "используй функцию get_news. Никогда не выдумывай новости самостоятельно. "
        "Отвечай кратко, перечисляя заголовки с источником и датой. "
        "Если пользователь не указал тему, вежливо уточни её."
    )

    def __init__(self, registry: ToolRegistryProtocol, llm: LLMClientProtocol):
        self.tools = registry
        self.llm = llm

    def run(self, user_message: str) -> str:
        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
        response = self.llm.create_completion(
            messages,
            tools=self.tools.get_all_specs()
        )
        msg = response.choices[0].message

        if not msg.tool_calls:
            return msg.content or ""
        messages.append(msg)
        for tool_call in msg.tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            result = self.tools.execute(tool_name, **arguments)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })

        final = self.llm.create_completion(messages, temperature=0.3)
        return final.choices[0].message.content or ""