import os
from langchain.chat_models import ChatGroq
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()

def call_llm(prompt: str) -> str:
    groq_key = os.getenv("GROQ_API_KEY")
    llm = ChatGroq(api_key=groq_key, model="mixtral-8x7b-32768")  # or use llama3
    messages = [HumanMessage(content=prompt)]
    response = llm(messages)
    return response.content
