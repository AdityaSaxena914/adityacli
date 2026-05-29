from session import load_session, save_session, delete_session, session_exists
from config import load_system_prompt
from llm import get_client
from chat import stream_response
from ui import console, WELCOME_PANEL


client = get_client()
system_prompt = load_system_prompt()
conversation_history = [] #stores whole conversation history of one session

console.print(WELCOME_PANEL)

if session_exists():
    while True:
        res = input("Resume previous session? (y/n): ").strip().lower()
        if(res == "y"):
            conversation_history = load_session()
            break
        elif(res == "n"):
            delete_session()
            conversation_history = []
            break
        else:
            console.print("[red]Please enter y or n.[/red]")


while True:
    user_prompt = input("\nYou > ")
    if user_prompt.strip().lower() == "exit":
        break
    conversation_history.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ] + conversation_history
    assistant_response = stream_response(client, messages)
    
    conversation_history.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )
    save_session(conversation_history)
    print()
            

console.print("[yellow]Goodbye Aditya....[/yellow]")