from langchain.tools import tool
from utils.db_helper import execute_query
from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

DB_PATH = "databases/institutions.db"


def generate_sql(question: str):
    prompt = f"""
You are an SQL expert.

Table: institutions

Columns:
name, eiin, institution_type, division, district, thana, address, mobile, education_level

Return ONLY SQL query.

Question: {question}
"""
    return llm.invoke(prompt).content.strip()


@tool
def institution_tool(question: str) -> str:
    """Search for educational institutions in Bangladesh by name, district, division, type, or education level."""

    try:
        sql = generate_sql(question)
        columns, rows = execute_query(DB_PATH, sql)

        return {
            "sql": sql,
            "result": [dict(zip(columns, r)) for r in rows]
        }

    except Exception as e:
        return str(e)