MODEL_NAME = "qwen/qwen3.5-9b"
BASE_URL = "http://127.0.0.1:1234/v1"
API_KEY = "lm-studio"

SYSTEM_PROMPT_PATH = "prompts/system.txt"


def load_system_prompt():
    with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as file:
        return file.read()