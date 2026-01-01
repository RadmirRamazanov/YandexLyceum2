import sqlite3

genre = input()
con = sqlite3.connect("music_db.sqlite")
cur = con.cursor()
result = cur.execute(f"""SELECT DISTINCT
artist.Name
FROM
track,
album,
artist
INNER JOIN genre
ON genre.GenreId = track.GenreId AND album.AlbumId = track.AlbumId AND genre.Name = '{genre}'
AND artist.ArtistId = album.ArtistId
ORDER BY artist.Name""").fetchall()
for elem in result:
    print(*elem)
con.close()