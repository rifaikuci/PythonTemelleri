
import sqlite3

connection = sqlite3.connect("chinook.db")


connection.execute("Delete from customers where City= 'London'")
connection.commit()
connection.close()