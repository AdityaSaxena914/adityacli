import json
import os


def session_exists() -> bool:
    """Check if the current session exists by verifying the presence of the session file."""
    return os.path.exists("sessions/session.json")


def load_session():
    """Load and parse the conversation history from the session JSON file.
    
    Returns an empty list if the session file does not exist or cannot be read.
    """
    if not os.path.exists("sessions/session.json"):
        return []
    with open("sessions/session.json", "r") as file:
        try:
            return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []


def save_session(conversation_history):
    """Save the conversation history to the session JSON file.
    
    Args:
        conversation_history: A list or dictionary representing the chat data to be saved.
        
    Note: This function overwrites any existing content in 'sessions/session.json'.
    """
    with open("sessions/session.json", "w") as file:
        json.dump(conversation_history, file, indent=4)


def delete_session():
    """Delete the current session by removing the session JSON file.
    
    If the file does not exist, this function performs no action and returns silently.
    """
    if os.path.exists("sessions/session.json"):
        os.remove("sessions/session.json")