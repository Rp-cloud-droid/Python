import sqlite3
import pandas as pd

database = "database.sqlite"
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

cursor.execute("""
CREATE TABLE IF NOT EXISTS player (
               Player_Id INTEGER PRIMARY KEY,
               Player_Name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS season (
               Season_Id INTEGER PRIMARY KEY,
               Man_of_the_Series INTEGER,
               FOREIGN KEY (Man_of_the_Series) REFERENCES player (Player_Id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS team (
               Team_Id INTEGER PRIMARY KEY,
               Team_Name TEXT
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

cursor.executemany("INSERT OR IGNORE INTO player VALUES (?, ?)", [
    (1, 'Virat Kohli'),
    (2, 'Steve Smith'),
    (3, 'Joe Root')
])

cursor.executemany("INSERT OR IGNORE INTO season VALUES (?, ?)", [
    (1, 1),
    (2, 2)
])

cursor.executemany("INSERT OR IGNORE INTO team VALUES (?, ?)", [
    (1, 'India Team'),
    (2, 'Australia Team')
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

joined_left = pd.read_sql("""
SELECT *
FROM player
LEFT JOIN season
ON player.Player_Id = season.Man_of_the_Series                          
""", conn)
print("LEFT JOIN Result:")
print(joined_left, "\n")

joined_cross = pd.read_sql("""
SELECT c.Country_Name, ci.City_Name
FROM country c
CROSS JOIN city ci
""", conn)
print("CROSS JOIN Result:")
print(joined_cross, "\n")

union = pd.read_sql("""
SELECT Player_Name AS Name FROM player
UNION
SELECT Team_Name AS Name FROM team
""", conn)
print("UNION Result:")
print(union, "\n")

conn.close()