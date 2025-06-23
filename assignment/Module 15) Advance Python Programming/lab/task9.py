import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")

cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", ("Divyesh", 21, "Python"))
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", ("Aarav", 22, "Data Science"))

conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\nStudent Records:")
for row in rows:
    print(row)

conn.close()
