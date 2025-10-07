import sqlite3
import pandas as pd

conn = sqlite3.connect('example.sqlite')

cursor = conn.cursor()

print("Database created and connected successfully!")
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')

conn.commit()
print("Table created successfully!")
cursor.execute("INSERT INTO Students (name, age, grade) VALUES (?, ?, ?)",
               ('Rahul', 15, '10th'))
cursor.execute("INSERT INTO Students (name, age, grade) VALUES (?, ?, ?)",
               ('Sneha', 14, '9th'))
cursor.execute("INSERT INTO Students (name, age, grade) VALUES (?, ?, ?)",
               ('Arjun', 16, '11th'))

conn.commit()
print("Data inserted successfully!")
cursor.execute("SELECT * FROM Students")
rows = cursor.fetchall()

print("Student records:")
for row in rows:
    print(row)
conn.close()

conn = sqlite3.connect('example.sqlite')
df = pd.read_sql("SELECT * FROM Students", conn)
print(df)
