import pandas as pd
import sqlite3

database = 'db'

conn = sqlite3.connect(database)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Match 2 (
               Match_Id INTEGER PRIMARY KEY AUTOINCREMENT, 
               Season_Id INTEGER,
               Match_Winner TEXT,
               Win_Margin REAL,
               Man_of_the_Match TEXT,
               Venue_Id INTEGER
);
""")

print("Table 'Match 2' checked/created successfully ")

sample_data = [
    (1, 'Team A', 45, 'Player 1', 101),
    (2, 'Team B', 22, 'Player 2', 102),
    (2, 'Team A', 10, 'Player 3', 101),
    (3, 'Team C', 60, 'Player 1', 103),
]
conn.executemany("""
INSERT INTO Match 2 (Season_Id, Match_Winner, Win_Margin, Man_of_the_Match, Venue_Id)
VALUES (?, ?, ?, ?, ?);
""", sample_data)
conn.commit()
print("Sample data inserted ")

tables = pd.read_sql("""
SELECT name
FROM sqlite_master
WHERE type='table';
""", conn)
print("\n Tables in Database:")
print(tables)

matches = pd.read_sql("SELECT * FROM Match 2;", conn)
print("\n Match table preview:")
print(matches.head())



result1 = pd.read_sql("""
SELECT Match_Winner, AVG(Win_Margin) AS Avg_Win_Margin
FROM Match 2
WHERE Season_Id = 1
GROUP BY Match_Winner
ORDER BY Avg_Win_Margin;
""", conn)
print("\nAverage Win Margin (Season 1):")
print(result1)

result2 = pd.read_sql("""
SELECT COUNT(DISTINCT Venue_Id) AS Venue_Count
FROM Match 2
WHERE Season_Id = 2;
""", conn)
print("\nVenue Count (Season 2):")
print(result2)

result3 = pd.read_sql("""
SELECT
    MIN(Win_Margin) AS Min_Win_Margin,
    MAX(Win_Margin) AS Max_Win_Margin,
    AVG(Win_Margin) AS Avg_Win_Margin,
    COUNT(DISTINCT Man_of_the_Match) AS Unique_MOM_Count
FROM Match 2;
""", conn)
print("\n Stats Accross All Seasons:")
print(result3)

result4 = pd.read_sql("""
SELECT SUM(Win_Margin) AS Total_Win_Margin
FROM Match 2
WHERE Season_Id = 3;
""", conn)
print("\nTotal Win Margin (Season 3):")
print(result4)


conn.close()
print("\nDatabase connection closed ")