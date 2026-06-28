from langchain.tools import tool
from utils.db_helper import execute_query
from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

DB_PATH = "databases/restaurants.db"


def generate_sql(question: str):
    prompt = f"""
You are an SQL expert.

Table: restaurants

Columns:
name, latitude, longitude, rating, number_of_reviews, address

Return ONLY SQL query.

Question: {question}
"""
    return llm.invoke(prompt).content.strip()


@tool
def restaurant_tool(question: str) -> str:
    """Search for restaurants in Bangladesh by name, location, rating, or address."""

    try:
        sql = generate_sql(question)
        columns, rows = execute_query(DB_PATH, sql)

        return {
            "sql": sql,
            "result": [dict(zip(columns, r)) for r in rows]
        }

    except Exception as e:
        return str(e)