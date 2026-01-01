import sqlite3


con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT DISTINCT g.title   
    FROM genres g  
    JOIN films f ON g.id = f.genre  
    WHERE f.year IN (2010, 2011) """).fetchall()
for elem in result:
    print(*elem)
con.close()