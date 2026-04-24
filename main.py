from src.config import llm_client
from src.tools.tool_registry import ToolRegistry
from src.tools.news import NewsTool
from src.agent import NewsAgent

def build_agent() -> NewsAgent:
    registry = ToolRegistry()
    registry.register(NewsTool())
    return NewsAgent(registry, llm_client)

if __name__ == "__main__":
    agent = build_agent()
    print("AI-агент для новостей (Трек A)")
    print("Примеры: 'Новости о космосе', 'Что нового в мире ИИ?'")
    print("Введите запрос (или 'exit' для выхода):")
    while True:
        user_input = input("\n> ")
        if user_input.strip().lower()== "exit":
            break
        print("\nАгент:", agent.run(user_input))
