import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.main_agent import executor

def run_agent(question: str):
    try:
        res = executor.invoke({"input": question})
        return res["output"] if "output" in res else str(res)
    except Exception as e:
        return f"Error: {str(e)}"