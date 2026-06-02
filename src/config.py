MODEL_NAME = "qwen/qwen3.5-9b"
BASE_URL = "http://127.0.0.1:1234/v1"
API_KEY = "lm-studio"

SYSTEM_PROMPT_PATH = "prompts/system.txt"
EXPLAIN_PROMPT_PATH = "prompts/explain_file.txt"
PROJECT_EXPLAIN_PROMPT_PATH = "prompts/project_explain.txt"
REVIEW_PROMPT_PATH = "prompts/review_file.txt"
TEST_PROMPT_PATH = "prompts/generate_tests.txt"
DIFF_PROMPT_PATH = "prompts/diff.txt"



def load_prompt(prompt_path):
    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()