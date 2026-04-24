import os
from dotenv import load_dotenv
from openai import OpenAI
from src.llm.client import OpenAICompatibleClient

load_dotenv()

API_KEY = os.getenv("APIKEY")
ENDPOINT = os.getenv("ENDPOINT")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

if API_KEY:
    api_key = API_KEY
    base_url = ENDPOINT         
    model = "qwen3.5-122b"                     
else:
    raise RuntimeError(
        "Не найден ни один LLM API ключ. "
    )

openai_client = OpenAI(api_key=api_key, base_url=base_url)
llm_client = OpenAICompatibleClient(openai_client, model)