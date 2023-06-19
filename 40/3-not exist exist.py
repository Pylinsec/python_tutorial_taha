import sqlite3
#  exist , not exist  --> tRUE 
db = sqlite3.connect('chinook.db')
data = db.execute("SELECT CustomerId,FirstName,country FROM customers WHERE EXISTS (SELECT * FROM customers WHERE CustomerId >=35 ) ORDER BY CustomerId DESC")
data = db.execute("SELECT CustomerId,FirstName,country FROM customers WHERE 'USA' IN (SELECT country FROM customers  ) ORDER BY CustomerId DESC")
counter = 0
for row in data:
    counter += 1
    print(f"{counter}-->{row}")