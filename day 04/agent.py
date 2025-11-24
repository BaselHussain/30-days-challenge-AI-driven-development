from dotenv import load_dotenv
import os
from agents import Agent, OpenAIChatCompletionsModel, Runner
from openai import AsyncOpenAI
from tools import extract_pdf_text

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

MODEL_NAME="gemini-2.0-flash"
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
    
external_client=AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    
gemini_model=OpenAIChatCompletionsModel(
        model=MODEL_NAME,
        openai_client=external_client
    )

# System prompt
SYSTEM_PROMPT = "You are a precise academic assistant. Summarize PDFs accurately and generate quizzes using only the complete original text."

# Create the agent
academic_assistant_agent = Agent(
    name="Academic Assistant",
    instructions=SYSTEM_PROMPT,
    model=gemini_model
)

