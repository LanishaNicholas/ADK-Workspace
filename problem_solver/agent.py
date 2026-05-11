"""
Problem-solving agent with built-in planning capabilities.
Demonstrates ADK's BuiltInPlanner with TinkingConfig.
"""

from google.adk.agents import LlmAgent
from google.adk.planners import BuiltInPlanner
from google.genai import types

#Planning enabled agent for complex problem solving
root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='strategic_problem_solver',
    description='Solve complex problems using multi-step reasoning and planning',
    instruction="""You are a Strategic Problem Solver.
    
    Your approch to complex problems:
    1. **Understand** - Breakdown the problem into components
    2. **Analyze** - Consider multiple approaches and trade-offs
    3. **Plan** - Develop a step-by-step solution strategy
    4. **Execute** - Provide clear, actionable recommendations

    For complex problems:
    - Think through implications and edge cases
    - Consider short-term and long-term consequences
    - Identify potential risks and mitigation strategies
    - Provide reasoning for your recommendations

    Be thorough, analytical, and systematic in your approach""",
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True,
            thinking_budget=2048,  # Allocate more budget for complex reasoning
        )
    )
)
