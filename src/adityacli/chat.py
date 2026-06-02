from adityacli.config import MODEL_NAME


def stream_response(client, messages):
    assistant_response = ""
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages =messages,
        max_tokens = 4096,
        stream=True
    )

    print("\n[green]AdityaCLI[/green] > ",end=" ")
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)
            assistant_response += content
    print()
    return assistant_response

def get_completion(client, messages):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        max_tokens = 4096
    )

    return response.choices[0].message.content