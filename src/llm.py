from openai import OpenAI
from config import API_KEY, BASE_URL

def get_client():
    return OpenAI(
        base_url=BASE_URL,
        api_key=API_KEY
    )
