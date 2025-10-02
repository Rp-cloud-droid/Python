import pandas as pd
import sqlite3

database = 'databse.sqlite'

conn = sqlite3.connect(database)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    experience TEXT
);
""")

cursor.execute("INSERT INTO employees (name, age, experience) VALUES (?, ?, ?)", ('Jade', 18))
cursor.execute("INSERT INTO employees (name, age, experience) VALUES (?, ?, ?)", ('Jeremy', 21))
cursor.execute("INSERT INTO employees (name, age, experience) VALUES (?, ?, ?)", ('Frank', 19))

conn.commit()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
print("Using cursor.fetchall():", rows)

df = pd.read_sql("SELECT * FROM employees", conn)
print("\nUsing pandas DataFrame:")
print(df)

conn.close()