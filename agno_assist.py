from agno.agent import Agent
from agno.models.groq import Groq
from agno.os import AgentOS
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.models.openai import OpenAIChat


from dotenv import load_dotenv
import os

load_dotenv()

# search agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="openai/gpt-oss-120b"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    # show_tool_calls=True, removed from new agentos
    markdown=True,

)

# finance agent
finance_agent = Agent(
    name="Finance AI Agent",
    model = Groq(id="openai/gpt-oss-120b"),
    tools=[YFinanceTools(enable_stock_price=True,enable_analyst_recommendations=True,enable_stock_fundamentals=True,enable_company_news=True)],
    instructions=["Use tables to display the data"],
    # show_tool_calls=True, removed from new agentos
    markdown=True,
)

# initializing agent
agent_os = AgentOS(agents=[web_search_agent,finance_agent])
app = agent_os.get_app()

if __name__ == "__main__":
    # Serve the app locally
    agent_os.serve(app="agno_assist:app", reload=True)