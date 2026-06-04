from pathlib import Path


MODEL_NAME = "qwen/qwen3.5-9b"
BASE_URL = "http://127.0.0.1:1234/v1"
API_KEY = "lm-studio"


BASE_DIR = Path(__file__).resolve().parents[3]

PROMPTS_DIR = BASE_DIR / "prompts"

SYSTEM_PROMPT_PATH = PROMPTS_DIR / "system.txt"
EXPLAIN_PROMPT_PATH = PROMPTS_DIR / "explain_file.txt"
PROJECT_EXPLAIN_PROMPT_PATH = PROMPTS_DIR / "project_explain.txt"
REVIEW_PROMPT_PATH = PROMPTS_DIR / "review_file.txt"
TEST_PROMPT_PATH = PROMPTS_DIR / "generate_tests.txt"
DIFF_PROMPT_PATH = PROMPTS_DIR / "diff.txt"
CREATE_FILE_PROMPT_PATH = PROMPTS_DIR / "create_file.txt"
EDIT_FILE_PROMPT_PATH = PROMPTS_DIR / "edit_file.txt"
SEARCH_SUMMARY_PROMPT_PATH = PROMPTS_DIR / "search_summary.txt"

def load_prompt(prompt_path):
    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()
