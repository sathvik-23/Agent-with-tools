import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check for both possible keys
gemini_api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if gemini_api_key is None:
    raise ValueError("GEMINI_API_KEY or GOOGLE_API_KEY not found in environment variables")

# Set it explicitly in the environment
os.environ["GOOGLE_API_KEY"] = gemini_api_key

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools

# Initialize the agent with the Gemini model
agent = Agent(
    model=Gemini(id="gemini-1.5-flash", api_key=gemini_api_key),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

# Print the agent's response to the query (streaming enabled)
agent.print_response("Give me bengaluru news from THE HINDU also give relevant links", stream=True)
