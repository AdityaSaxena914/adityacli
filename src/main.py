from session import load_session, save_session, delete_session, session_exists
from config import load_prompt
from llm import get_client
from chat import stream_response
from ui import console, header_panel,render_dashboard


def run_chat():
    client = get_client()
    system_prompt = load_prompt()
    conversation_history = [] #stores whole conversation history of one session


    header_panel()

    session_loaded = False
    if session_exists():
        while True:
            res = input("Resume previous session? (y/n): ").strip().lower()
            print("\n\n")
            if(res == "y"):
                conversation_history = load_session()
                session_loaded = True
                break
            elif(res == "n"):
                delete_session()
                conversation_history = []
                break
            else:
                console.print("[red]Please enter y or n.[/red]")

    render_dashboard(
        session_loaded=session_loaded,
        message_count=len(conversation_history)
    )

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


if __name__ == "__main__":
    run_chat()