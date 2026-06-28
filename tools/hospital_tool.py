from langchain.tools import tool
from utils.db_helper import execute_query
from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

DB_PATH = "databases/hospitals.db"


def generate_sql(question: str):
    prompt = f"""
You are an expert SQL generator.

Database table: hospitals
Columns:
id, name, name_bangla, code, agency, type, division, district, city_corporation, upazila, paurasava, union_name, private

Rules:
- Return ONLY SQL query
- No explanation
- Use correct SQLite syntax

Question: {question}
"""

    response = llm.invoke(prompt)
    return response.content.strip()


@tool
def hospital_tool(question: str):
    """
    Use this tool for hospital related questions.
    Input: natural language question
    """

    try:
        sql = generate_sql(question)

        columns, rows = execute_query(DB_PATH, sql)

        if not rows:
            return "No data found."

        result = [dict(zip(columns, row)) for row in rows]

        return {
            "sql": sql,
            "result": result
        }

    except Exception as e:
        return str(e)