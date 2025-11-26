import sqlite3


con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT title FROM films
    WHERE duration >= 60 AND genre=(
SELECT id FROM genres
    WHERE title = 'комедия')""").fetchall()
for elem in result:
    print(*elem)
con.close()