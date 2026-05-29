import json
import os

def session_exists():
    return os.path.exists("sessions/session.json")

def load_session():
    if not os.path.exists("sessions/session.json"):
        return []
    with open("sessions/session.json", "r") as file:
        return json.load(file)

def save_session(conversation_history):
    with open("sessions/session.json", "w") as file:
        json.dump(conversation_history, file, indent=4)

def delete_session():
    if os.path.exists("sessions/session.json"):
        os.remove("sessions/session.json")