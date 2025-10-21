import sqlite3
import pandas as pd

conn = sqlite3.connect('ipl_teams.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Teams (
               Team_Id INTEGER PRIMARY KEY,
               Team_Name TEXT NOT NULL
               );
''')

teams = [
    (1, "Kolkata Knight Riders"),
    (2, "Royal Challengers Banglore"),
    (3, "Chennai Super Kings"),
    (4, "Kings XI Punjab"),
    (5, "Rajastan Royals")
]

cursor.executemany('INSERT OR IGNORE INTO Teams (Team_Id, Team_Name) VALUES (?, ?)', teams)
conn.commit()

query = '''
SELECT * FROM Teams
WHERE Team_Id > (
SELECT AVG(Team_Id) FROM Teams
);
'''

teams_df = pd.read_sql(query, conn)
print("Teams with Team_Id greater than average Team_Id:")
print("teams_df")

conn.close()