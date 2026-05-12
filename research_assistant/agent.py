"""
Research Assistant Agent
Demonstrates ADK's Google Search built-in tool for real-time information.
Reference: https://google.github.io/adk-docs/tools/built-in-tools#google-search
"""

from google.adk.agents import LlmAgent
from google.adk.tools import google_search # Import the Google Search tool


root_agent = LlmAgent(
    model='gemini-2.5-flash', #must be a Gemini 2.5 model to use the Google Search tool
    name='research_assistant',
    description='Helps users research topics using Google Search.',
    instruction="""
    You are a research assistant that helps users find accurate, up-to-date information.

    Your Approach:
        1. When user ask questions requiring current information, use Google Search
        2. Base your answers on the search results
        3. Cite sources when providing information
        4. If search results are insufficient, acknowledge limitations

        Always prioritize accuracy over speculation. If you'e unsure, say so.
    """,
    tools=[google_search]
)
