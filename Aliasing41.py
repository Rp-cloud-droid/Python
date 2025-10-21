import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE City (
               City_Id INTEGER PRIMARY KEY,
               City_Name TEXT
);
""")

cursor.execute("""
CREATE TABLE Venue (
               Venue_Id INTEGER PRIMARY KEY,
               Venue_Name TEXT,
               City_Id INTEGER,
               FOREIGN KEY(City_Id) REFERENCES City(City_Id)
);
""")

cursor.execute("""
CREATE TABLE Team (
               Team_Id INTEGER PRIMARY KEY,
               Team_Name TEXT
);
""")

cursor.execute("""
CREATE TABLE Match (
               Match_Id INTEGER PRIMARY KEY,
               Season_Id INTEGER,
               Venue_Id INTEGER,
               Match_Winner INTEGER,
               FOREIGN KEY (Venue_Id) REFERENCES Venue(Venue_Id),
               FOREIGN KEY (Match_Winner) REFERENCES Team(Team_Id)
);
""")

cursor.executemany("INSERT INTO City VALUES (?, ?)" ,[
    (1, 'Dehli'),
    (2, 'Mumbai')
])

cursor.executemany("INSERT INTO Venue VALUES (?, ?, ?)" ,[
    (1, 'Feroz Shah Kotla', 1),
    (2, 'Wankhede Stadium', 2)
])

cursor.executemany("INSERT INTO Team VALUES (?, ?)" ,[
    (1, 'Dehli Capitals'),
    (2, 'Mumbai Indians')
])

cursor.executemany("INSERT INTO Match VALUES (?, ?, ?, ?)" ,[
    (101, 2020, 1, 1),
    (102, 2020, 2, 2)
])

conn.commit()

query = '''
SELECT
m.Season_Id,
m.Match_Id,
v.Venue_Name,
c.City_Name,
t.Team_Name AS Winner
FROM Match AS m
INNER JOIN Venue AS v ON m.Venue_Id = v.Venue_Id
INNER JOIN City AS c ON v.City_Id = c.City_Id
INNER JOIN Team AS t ON m.Match_Winner = t.Team_Id;
'''

match_details = pd.read_sql(query, conn)

print(match_details)