import sqlite3

def execute_query(database_path, query):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    columns = [description[0] for description in cursor.description]

    conn.close()

    return columns, rows