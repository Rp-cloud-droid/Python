import sqlite3
import pandas as pd

database = "cricket_database.sqlite"
conn = sqlite3.connect(database)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Cricket_Match (
    Match_Id INTEGER,
    Player_Id INTEGER,
    Runs INTEGER,
    Wickets INTEGER,
    Catches INTEGER
);
""")
print("Table 'Cricket_Match' created successfully!")

cursor.executemany("""
INSERT INTO Cricket_Match (Match_Id, Player_Id, Runs, Wickets, catches)
                   VALUES (?, ?, ?, ?, ?)
""", [
    (1, 101, 45, 1, 0),
    (1, None, 70, 0, 1),
    (2, 101, None, 2, 1),
    (2, 103, 55, 0, None),
    (3, 104, 60, 3, 2),
    (3, 105, None, None, None)
])
conn.commit()
print("Sample data inserted successfully!")

cricket_match = pd.read_sql("SELECT * FROM Cricket_Match", conn)

print("\nFirst 5 rows of Cricket_Match table:")
print(cricket_match.head())

print("\nChecking for NULL (missing) values:")
null_summary = cricket_match.isnull().sum()

print(null_summary)

print("\nColumns containing NULL values:")
print(null_summary[null_summary > 0])

conn.close()
print("\nDatabase connection closed successfully!")
