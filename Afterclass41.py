import sqlite3
import pandas as pd

database = "db.sqlite"
conn = sqlite3.connect(database)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS country (
               Country_Id INTEGER PRIMARY KEY,
               Country_Name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS city (
               City_Id INTEGER PRIMARY KEY,
               City_Name TEXT,
               Country_Id INTEGER,
               FOREIGN KEY (Country_Id) REFERENCES country (Country_Id)
)
""")

cursor.executemany("INSERT OR IGNORE INTO country VALUES (?, ?)", [
    (1, 'India'),
    (2, 'Australia'),
    (3, 'England')
])

cursor.executemany("INSERT OR IGNORE INTO city VALUES (?, ?, ?)", [
    (1, 'Dehli', 1),
    (2, 'Sydney', 2),
    (3, 'London', 3)
])

conn.commit()

tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
print("Tables in the database:")
print(tables, "\n")

joined_city = pd.read_sql("""
SELECT c.Country_Id, c.Country_Name, ci.City_Name
FROM country c
INNER JOIN city ci ON c.Country_Id = ci.Country_Id
""", conn)
print("INNER JOIN Result:")
print(joined_city, "\n")

conn.close()