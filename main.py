from langchain.agents import create_agent
from langchain.tools import tool
from langchain_anthropic import ChatAnthropic
from tools import get_key_places, get_weather
from dotenv import load_dotenv
import getpass
import os
from langchain.messages import (
    HumanMessage,
    SystemMessage,
)

load_dotenv()

if not os.getenv("ANTHROPIC_API_KEY"):
    os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("Enter your Hugging Face API token: ")

llm = ChatAnthropic(model="claude-3-haiku-20240307")#, anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"))

# User input example
input_prompt = "Plan a bike trip from Pune to Mumbai with preferred good weather for 17 Nov 2025."



# Initialize a LangChain agent that uses these tools intelligently
# agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
agent = create_agent(
    model=llm,
    tools=[get_key_places, get_weather],
)


# Agent runs and decides which tool to call in sequence, reasons, and returns a plan
response = agent.invoke({
    "messages" : [
    SystemMessage(content="You are a helpful assistant. You have access to tools to get route information and weather forecasts. Use them wisely to help the user plan their trip. And provide the final plan based on the data you gather with right time to start the trip, and rest stops along the way."),
    HumanMessage(content=input_prompt)
]
})

print(response)
try:
    with open('output.txt', 'w') as f:
        f.write(str(response))
except Exception as e:
    print(f"Error writing to file: {e}")
