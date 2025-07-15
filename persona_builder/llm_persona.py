import requests

# Ollama config (local LLM inference)
OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "phi"  # or "mistral" if you've pulled it

def generate_persona(username, chunks):
    personas = []

    for i, chunk in enumerate(chunks):
        print(f"Generating persona block {i + 1} of {len(chunks)}...")

        prompt = f"""
You're an intelligent assistant tasked with generating a user persona.

Given the Reddit content below, analyze and generate a persona block with:
- 2 personality traits
- Writing style description
- Topic interests
- 2 quoted examples
- A short summary paragraph

Respond in this format:

Username: u/{username}

Personality Traits:
1. ...
2. ...

Writing Style:
...

Topic Interests:
...

Quotes:
- "..."
- "..."

Generated Summary:
...

Reddit Content:
\"\"\"
{chunk}
\"\"\"
"""

        try:
            res = requests.post(OLLAMA_API_URL, json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            })

            response_text = res.json()["response"].strip()
            personas.append(response_text)

        except Exception as e:
            personas.append(f"[ERROR generating persona: {e}]")

    return personas
