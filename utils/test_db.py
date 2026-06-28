import sqlite3

conn = sqlite3.connect("databases/hospitals.db")

cursor = conn.cursor()

cursor.execute("SELECT name,district,type FROM hospitals LIMIT 5")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()