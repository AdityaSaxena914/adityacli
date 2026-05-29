from openai import OpenAI
from session import load_session, save_session, delete_session, session_exists



#giving custom prompt to the local model
with open("prompts/system.txt", "r", encoding="utf-8") as file:
    system_prompt = file.read()

conversation_history = [] #stores whole conversation history of one session

print("Welcome to AdityaCLI.\n")

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
            print("Please enter y or n.")


while True:
    assistant_response = ""
    user_prompt = input("\nYou > ")
    if user_prompt.strip().lower() == "exit":
        break
    conversation_history.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )


    response = client.chat.completions.create(
        model="qwen/qwen3.5-9b",
        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]+conversation_history,
        stream=True
    )

    print("\nAI >")
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)
            assistant_response += content
    conversation_history.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )
    save_session(conversation_history)
    print()
            

print("Goodbye Aditya....")