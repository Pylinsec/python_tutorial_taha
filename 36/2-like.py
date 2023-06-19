import sqlite3
db = sqlite3.Connection("chinook.db")
# data = db.execute("SELECT CustomerId , Country FROM Customers WHERE Country LIKE 'U%'")# % --> tedad harchizi az 0 ta binahayat 
data = db.execute("SELECT CustomerId , Country FROM Customers WHERE Country LIKE '___'")# % --> tedad harchizi az 0 ta binahayat 

for row in data:
    print(f"id ---> {row}")