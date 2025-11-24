from dotenv import load_dotenv
import os
from agents import Agent, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from tools import extract_pdf_text

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

# Create OpenAI-compatible client with Gemini base URL
openai_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=GEMINI_API_KEY,
)

# Instantiate OpenaiChatCompletionModel
gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=openai_client
)

# System prompt
SYSTEM_PROMPT = "You are a precise academic assistant. First extract text from pdf and then Summarize PDFs accurately and generate quizzes using only the complete original text."

# Create the agent
academic_assistant_agent = Agent(
    name="Academic Assistant",
    instructions=SYSTEM_PROMPT,
    tools=[extract_pdf_text],
    model=gemini_model
)
