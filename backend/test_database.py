import sqlite3

connection = sqlite3.connect("../data/research.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT persona_name, question, answer
    FROM interviews
    ORDER BY id DESC
    LIMIT 5
""")

rows = cursor.fetchall()

for row in rows:
    print("\nPersona:", row[0])
    print("Question:", row[1])
    print("Answer:", row[2])

connection.close()