import json
import requests
from src.config import NEWSAPI_KEY
from src.tools.base import ToolProtocol

class NewsTool(ToolProtocol):
    @property
    def name(self) -> str:
        return "get_news"

    @property
    def description(self) -> str:
        return "Получить последние новости по заданной теме на русском языке"

    @property
    def parameters(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "Тема для поиска новостей, например 'спорт', 'искусственный интеллект'"
                }
            },
            "required": ["topic"]
        }

    @property
    def openai_spec(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters
            }
        }

    def execute(self, **kwargs) -> str:
        topic = kwargs.get("topic", "")
        url = "https://newsapi.org/v2/everything"
        params = {
            "q": topic,
            "pageSize": 5,
            "apiKey": NEWSAPI_KEY,
            "language": "ru",
            "sortBy": "publishedAt"
        }
        try:
            r = requests.get(url, params=params, timeout=10)
            r.raise_for_status()
            articles = r.json().get("articles", [])
            results = [
                {
                    "title": a["title"],
                    "source": a["source"]["name"],
                    "date": a["publishedAt"][:10]
                }
                for a in articles
            ]
            return json.dumps(results, ensure_ascii=False)
        except Exception as e:
            return json.dumps({"error": f"Не удалось получить новости: {str(e)}"})