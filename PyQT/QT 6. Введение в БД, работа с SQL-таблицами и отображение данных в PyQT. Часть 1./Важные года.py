import sqlite3


con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT DISTINCT year FROM films
    WHERE title LIKE 'Х%'""").fetchall()
for elem in result:
    print(*elem)
con.close()