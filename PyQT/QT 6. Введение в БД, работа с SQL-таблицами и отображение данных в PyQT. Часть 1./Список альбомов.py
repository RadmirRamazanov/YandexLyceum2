import sqlite3

genre = input()
con = sqlite3.connect("music_db.sqlite")
cur = con.cursor()
result = cur.execute(f"""SELECT DISTINCT
    album.Title
FROM
    track,
    album
INNER JOIN genre
    ON genre.GenreId = track.GenreId AND album.AlbumId = track.AlbumId AND genre.Name = '{genre}'
ORDER BY album.ArtistId, album.Title""").fetchall()
for elem in result:
    print(*elem)
con.close()