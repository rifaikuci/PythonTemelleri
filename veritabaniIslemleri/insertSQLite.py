
import sqlite3

connection = sqlite3.connect("chinook.db")


connection.execute("Insert Into customers (FirstName,LastName,Email,City) values ('Rifai', 'Kuci', 'rfai07@gmail.com','Mardin')")
connection.commit()
connection.close()