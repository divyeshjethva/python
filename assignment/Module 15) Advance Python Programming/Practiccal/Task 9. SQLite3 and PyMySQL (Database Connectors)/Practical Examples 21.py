# 21) Write a Python program to create a database and a table using SQLite3.

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

print("Table 'students' created successfully!")


conn.commit()
conn.close()
