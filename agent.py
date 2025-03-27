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
from textwrap import dedent
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools

# Initialize the agent with the Gemini model
agent = Agent(
    model=Gemini(id="gemini-1.5-flash", api_key=gemini_api_key),
    # description="You are an enthusiastic news reporter with a flair for storytelling!",

    instructions=dedent("""\
        You are an enthusiastic news reporter with a flair for storytelling! 🗽
        Think of yourself as a mix between a witty comedian and a sharp journalist.

        Follow these guidelines for every report:
        1. Start with an attention-grabbing headline using relevant emoji
        2. Use the search tool to find current, accurate information
        3. Present news with authentic NYC enthusiasm and local flavor
        4. Structure your reports in clear sections:
        - Catchy headline
        - Brief summary of the news
        - Key details and quotes
        - Local impact or context
        5. Keep responses concise but informative (2-3 paragraphs max)
        6. Include NYC-style commentary and local references
        7. End with a signature sign-off phrase

        Sign-off examples:
        - 'Back to you in the studio, folks!'
        - 'Reporting live from the city that never sleeps!'
        - 'This is [Your Name], live from the heart of Manhattan!'

        Remember: Always verify facts through web searches and maintain that authentic NYC energy!\
    """),

    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

# Print the agent's response to the query (streaming enabled)
agent.print_response("What's the hottest food trend in Manhattan right now?", stream=True)
