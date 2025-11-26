import sqlite3


con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT title FROM films
    WHERE year >= 1997 AND genre IN (
SELECT id FROM genres
    WHERE title = "музыка" OR title = "анимация")""").fetchall()
for elem in result:
    print(*elem)
con.close()