from adityacli.core import MODEL_NAME
from adityacli.ui import console


def stream_response(client, messages):
    assistant_response = ""
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages =messages,
        max_tokens = 4096,
        stream=True
    )

    console.print("\n[bold green]AdityaCLI[/bold green] >", end=" ")
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