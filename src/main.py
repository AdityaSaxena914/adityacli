from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

user_prompt = input("You > ")

response = client.chat.completions.create(
    model="qwen/qwen3.5-9b",
    messages=[
        {
            "role": "user",
            "content": user_prompt
        }
    ]
)

print("\nAI >")
print(response.choices[0].message.content)