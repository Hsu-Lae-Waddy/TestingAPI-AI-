from prompts import generate_prompt
from groq_client import call_llm

def get_things_to_bring(destination: str, days: str) -> str:
    prompt = generate_prompt(destination, days)
    result = call_llm(prompt)
    return result
