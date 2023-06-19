import sqlite3

#  LIMIT 
db = sqlite3.connect("chinook.db")
# data = db.execute("SELECT CustomerId ,FirstName FROM customers ORDER BY FirstName DESC LIMIT 10")
# for row in data :
#     print(row)

# max on integer select MIN/MAX(col name)
data = db.execute("SELECT MIN(CustomerId) , FirstName FROM customers ORDER BY FirstName DESC")
data = db.execute("SELECT MAX(CustomerId) , FirstName FROM customers ORDER BY FirstName DESC")
data = db.execute("SELECT COUNT(Fax) FROM customers ORDER BY FirstName DESC")
for row in data :
    print(row)