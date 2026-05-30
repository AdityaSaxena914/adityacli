from config import MODEL_NAME


def stream_response(client, messages):
    assistant_response = ""
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages =messages,
        stream=True
    )

    print("\nAI >",end=" ")
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)
            assistant_response += content
    print()
    return assistant_response