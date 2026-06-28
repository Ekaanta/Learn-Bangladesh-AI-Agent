import sqlite3
from langchain.tools import tool

def run_sql(db_path: str, query: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description] if cursor.description else []

    conn.close()

    return columns, rows