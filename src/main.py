from openai import OpenAI

#creating client, we create only one client per session
client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)


#giving custom prompt to the local model
with open("prompts/system.txt", "r", encoding="utf-8") as file:
    system_prompt = file.read()


print("Welcome to AdityaCLI.\n")

while True:
    user_prompt = input("\nYou > ")
    if user_prompt.strip().lower() == "exit":
        break

    response = client.chat.completions.create(
        model="qwen/qwen3.5-9b",
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        stream=True
    )

    print("\nAI >")
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)
            

print("Goodbye Aditya....")