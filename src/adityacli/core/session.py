import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
SESSIONS_DIR = BASE_DIR / "sessions"
SESSION_PATH = SESSIONS_DIR / "session.json"


def session_exists() -> bool:
    """Check if the current session exists."""
    return SESSION_PATH.exists()


def load_session():
    """Load conversation history from session file."""
    if not SESSION_PATH.exists():
        return []

    try:
        with open(SESSION_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []


def save_session(conversation_history):
    """Save conversation history to session file."""
    SESSIONS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        SESSION_PATH,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            conversation_history,
            file,
            indent=4
        )


def delete_session():
    """Delete current session."""
    if SESSION_PATH.exists():
        SESSION_PATH.unlink()