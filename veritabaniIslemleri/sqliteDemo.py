import  sqlite3


connection = sqlite3.connect("chinook.db")

#cursor = connection.execute("select LastName,FirstName,CustomerId from customers where City='Berlin' or  City = 'Toronto'")
# cursor = connection.execute("""select LastName,FirstName,CustomerId
#                                 from customers ORDER BY LastName desc """) #sıralama işlemi
#
# for row in cursor:
#     print(str(row[2]) + " " + row[0] + "  " + row[1] )



# group by gruplama işlemini sağlıyor .
# having ise oluşan değerler ile işlemler yapılmasını sağlar.
# cursor = connection.execute("""Select city , count(Country)  from customers group by Country having count(Country) >3""")
#
#
# for row in cursor:
#     print("Sehir : " + row[0] )
#     print("Sayi : " +str( row[1]) )