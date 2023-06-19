import sqlite3

#  having 
#  jayegah : WHERE condtion --> GROUP BY column (HATMAN QABL AZ HAVING BAYAD BASHAD--> HAVING condition --> ORDER BY  column1 ,column 2 ASC/DESC
db = sqlite3.connect('chinook.db')
data = db.execute("SELECT FirstName,country , count(country) FROM customers GROUP BY country HAVING count(country) >3 ORDER BY count(country)")
data = db.execute("SELECT CustomerId,FirstName,country , count(country) FROM customers GROUP BY country HAVING CustomerId > 30 ORDER BY CustomerId")
for row in  data:
    print(row)
