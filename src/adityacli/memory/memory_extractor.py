import json
from adityacli.core.config import (
    load_prompt,
    MODEL_NAME,
    MEMORY_EXTRACTION_PROMPT_PATH
)

class MemoryExtractor:

    def __init__(self, client):

        self.client = client

    def extract(self, user_message, assistant_message):

        conversation = f"""
        User:
        {user_message}
        
        Assistant:
        {assistant_message}
        """
        
        memory_prompt = load_prompt(
            MEMORY_EXTRACTION_PROMPT_PATH
        )
        
        messages = [
            {
                "role": "system",
                "content": memory_prompt
            },

            {
                "role": "user",
                "content": conversation
            }
        ]
        
        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            max_tokens=512
        )
        content = response.choices[0].message.content
        return json.loads(content)