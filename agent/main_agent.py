import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"))

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate

from tools.hospital_tool import hospital_tool
from tools.institution_tool import institution_tool
from tools.restaurant_tool import restaurant_tool
from tools.web_search import web_search

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

tools = [
    hospital_tool,
    institution_tool,
    restaurant_tool,
    web_search
]

prompt = PromptTemplate.from_template("""
You are a Bangladesh AI assistant.

Use tools:
- hospital_tool → hospitals
- institution_tool → institutions
- restaurant_tool → restaurants
- web_search → general knowledge

Always pick the correct tool automatically.
Return clean answer only.

You have access to the following tools:
{tools}

Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
""")

agent = create_react_agent(llm, tools, prompt)

executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

if __name__ == "__main__":
    print("\nAI Agent Ready\n")

    while True:
        q = input("Ask: ")

        if q.lower() in ["exit", "quit"]:
            break

        res = executor.invoke({"input": q})
        print("\nAnswer:\n", res["output"])