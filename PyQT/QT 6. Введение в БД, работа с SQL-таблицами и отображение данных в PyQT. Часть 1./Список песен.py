import sqlite3

artist = input()
con = sqlite3.connect("music_db.sqlite")
cur = con.cursor()
result = cur.execute(f"""SELECT DISTINCT
    track.Name
FROM
    track,
    album
INNER JOIN artist
    ON artist.ArtistId = album.ArtistId AND artist.Name = '{artist}' AND album.AlbumId = track.AlbumId;""").fetchall()
ans = []
for elem in result:
    ans.append(*elem)
for i in sorted(ans):
    print(i)
con.close()