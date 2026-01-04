import sqlite3

conn = sqlite3.connect("zoo.db")
print("Database created and connected successfully")

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS animals (
    animal_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    age INTEGER
)
""")

print("Table created successfully")

conn.commit()
conn.close()
