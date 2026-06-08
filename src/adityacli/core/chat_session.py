from adityacli.core import (
    get_client,
    load_prompt,
    load_session,
    save_session,
    delete_session,
    session_exists,
    SYSTEM_PROMPT_PATH
)

from adityacli.ui import (
    console,
    header_panel,
    render_dashboard
)

from rich.prompt import Prompt

from adityacli.chat import stream_response

from adityacli.memory import (
    MemoryDB,
    MemoryExtractor,
    MemoryRetriever,
    ContextBuilder,
    MemoryManager
)

def run_chat():
    client = get_client()

    db = MemoryDB()
    retriever = MemoryRetriever(db)
    context_builder = ContextBuilder(
       retriever
    )

    memory_extractor = MemoryExtractor(
        client
    )

    memory_manager = MemoryManager(
        db,
        retriever,
        memory_extractor
    )
    
    system_prompt = load_prompt(SYSTEM_PROMPT_PATH)
    conversation_history = [] #stores whole conversation history of one session


    header_panel()

    session_loaded = False

    if session_exists():
        res = Prompt.ask(
            "[cyan]Resume previous session[/cyan]",
            choices=["y", "n", "Y", "N"],
            default="y"
        ).lower()

        print("\n")

        if res == "y":
            conversation_history = load_session()
            session_loaded = True
        else:
            delete_session()
            conversation_history = []

    render_dashboard(
        session_loaded=session_loaded,
        message_count=len(conversation_history)
    )

    while True:

        console.print()
        console.print("\n[cyan]You[/cyan] >", end=" ")
        user_prompt = input()


        if user_prompt.strip().lower() == "exit":
            break
        
        
        ucm = context_builder.build(user_prompt)
        
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
            },
            {
                "role": "system",
                "content": ucm.build_context()
            }
        ] + conversation_history
        
        
        assistant_response = stream_response(client, messages)
    
        conversation_history.append(
            {
                "role": "assistant",
                "content": assistant_response
            }
        )

        memory_manager.process_conversation(
            user_prompt,
            assistant_response
        )
        
        
        save_session(conversation_history)
        print()
    
    console.print(
        "\n[yellow]Session saved. Goodbye.[/yellow]"
    )


if __name__ == "__main__":
    run_chat()