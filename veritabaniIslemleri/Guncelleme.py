
import sqlite3

connection = sqlite3.connect("chinook.db")


connection.execute("Update customers set City='Mardin' where City='Rome' ")
connection.commit()
connection.close()