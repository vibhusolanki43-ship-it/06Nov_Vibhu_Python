import sqlite3

conn = sqlite3.connect("zoo.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS animals (
    animal_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    age INTEGER
)
""")

cur.execute("INSERT INTO animals (name, category, age) VALUES (?, ?, ?)",
            ("Lion", "Wild", 5))
cur.execute("INSERT INTO animals (name, category, age) VALUES (?, ?, ?)",
            ("Elephant", "Wild", 10))

conn.commit()
print("Data inserted successfully")

cur.execute("SELECT * FROM animals")
records = cur.fetchall()

print("\nAnimal Records:")
for row in records:
    print(row)

conn.close()
