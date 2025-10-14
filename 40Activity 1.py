import sqlite3

conn = sqlite3.connect("school.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS class10D (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    gender TEXT CHECK(gender IN('Male', 'Female', 'Other')),
    age INTEGER CHECK(age > 0),
    marks REAL CHECK(marks >= 0 AND marks <= 100)
);
""")

print("Database and table created successfully!")

students = [
    (1, 'Aarav Kumar', 'Male', 15, 92.5),
    (2, 'Diya Nair', 'Female', 14, 95.0),
    (3, 'Rahul Raj', 'Male', 15, 89.0),
    (4, 'Sneha Thomas', 'Female', 15, 97.2),
]

cursor.executemany("INSERT OR IGNORE INTO class10D VALUES (?, ?, ?, ?, ?)", students)
conn.commit()

cursor.execute("SELECT * FROM class10D")
rows = cursor.fetchall()

print("\nStudent Details in Class 10-D:")
print("Roll_No | Name | Gender | Age | Marks")
print("--------------------------------------")
for row in rows:
    print(row)


conn.close()
print("\nConnection closed successfully!")