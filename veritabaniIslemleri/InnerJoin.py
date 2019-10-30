


import sqlite3

connection = sqlite3.connect("chinook.db")


con = connection.execute("SELECT Title, Name from albums inner join  artists a on albums.ArtistId = a.ArtistId ")

for row in con:
    print(row[0]+ " - " + row[1])



connection.close()
