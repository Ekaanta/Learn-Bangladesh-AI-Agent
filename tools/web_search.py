from langchain.tools import tool
from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str):

    """
    Use this tool for general knowledge questions.
    """

    result = client.search(query=query)

    return result