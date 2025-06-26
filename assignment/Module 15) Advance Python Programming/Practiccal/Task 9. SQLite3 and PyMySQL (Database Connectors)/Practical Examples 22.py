# 22) Write a Python program to insert data into an SQLite3 database and fetch it.

import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
''')

cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Alice", 21))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Bob", 25))

conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

conn.close()