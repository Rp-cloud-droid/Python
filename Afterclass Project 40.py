import sqlite3

conn = sqlite3.connect("afterclass.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Suspects_List (
    suspect_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    gender TEXT CHECK(gender IN('Male', 'Female', 'Other')),
    age INTEGER CHECK(age > 0)
);
""")

print("Database and table created successfully!")

suspects = [
    (1, 'Ayaan Kumar', 'Male', 21),
    (2, 'Nick Nair', 'Male', 16),
    (3, 'Anushka Raj', 'Female', 18,),
    (4, 'Ari Thomas', 'Female', 15,),
]

cursor.executemany("INSERT OR IGNORE INTO Suspects_List VALUES (?, ?, ?, ?)", suspects)
conn.commit()

cursor.execute("SELECT * FROM Suspects_List")
rows = cursor.fetchall()

print("\nSuspect Details in Suspects List:")
print("Suspect_No | Name | Gender | Age")
print("---------------------------------")
for row in rows:
    print(row)


conn.close()
print("\nConnection closed successfully!")