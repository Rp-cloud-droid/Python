import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE Soccer Data (
    match_id INTEGER PRIMARY KEY,
    date TEXT,
    opponent_team TEXT,
    venue TEXT,
    mavericks_score INTEGER,
    opponent_score INTEGER,
    result TEXT -- 'Win', 'Loss', or 'Draw'
)
""")

sample_data = [
    (1, '2025-01-15', 'Tigers', 'Home', 240, 230, 'Win'),
    (2, '2025-01-22', 'Warriors', 'Away', 180, 220, 'Loss'),
    (3, '2025-02-01', 'Panthers', 'Home', 210, 210, 'Draw'),
    (4, '2025-02-10', 'Tigers', 'Away',260, 250, 'Win'),
    (5, '2025-02-20', 'Warriors', 'Home', 200, 199, 'Win')
]

cursor.executemany("""
INSERT INTO Soccer Data (match_id, date, opponent_team, venue, mavericks_score, opponent_score, result)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", sample_data)

conn.commit()

print("1. All Soccer data:")
df_all = pd.read_sql_query("SELECT * FROM Soccer Data", conn)
print(df_all)

print("\n2. Total matches played:")
cursor.execute("SELECT COUNT(*) FROM Soccer Data")
print("Total Matches:", cursor.fetchone()[0])

print("\n4. Matches played at Home:")
df_home = pd.read_sql_query("SELECT * FROM Matches WHERE venue = 'Home'", conn)
print(df_home)

print("\n5. Average score of Mavericks:")
cursor.execute("SELECT AVG(mavericks_score) FROM Soccer Data")
print("Average Score:", round(cursor.fetchone()[0], 2))

print("\n6. Win percentage:")
cursor.execute("SELECT 100.0 * SUM(CASE WHEN result = 'Win' THEN 1 ELSE 0 END) / COUNT(*) FROM Soccer Data")
print("Win %:", round(cursor.fetchone()[0], 2))

conn.close()
