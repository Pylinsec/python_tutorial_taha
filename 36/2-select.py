import sqlite3
db = sqlite3.Connection("chinook.db")
# data = db.execute("SELECT * FROM Customers WHERE CustomerId > 45") # 
# data = db.execute("SELECT * FROM Customers WHERE Country = 'USA'") # equal inja  = hastt

# distinct --> yani tekrai feghat yekbar biar 
# data = db.execute("SELECT DISTINCT Country FROM Customers WHERE Country <> 'USA'") # not equal <> 
# data = db.execute("SELECT CustomerId FROM Customers WHERE CustomerId < 10 ") # less than < <= 
# data = db.execute("SELECT CustomerId FROM Customers WHERE CustomerId > 50 ") # great than > >= 
# data = db.execute("SELECT CustomerId FROM Customers WHERE CustomerId  BETWEEN 50  AND 57") # BETWEEN value1 AND value2  -> IF VALUE 2 > VALUE1
# data = db.execute("SELECT CustomerId , Country FROM Customers WHERE Country  IN ('USA','Canada')") # IN  --> sootoon ba meqdar khas 
# data = db.execute("SELECT CustomerId , Country FROM Customers WHERE Country  NOT IN ('USA','Canada')") #NOT IN  --> sootoon ba meqdar BE JOZ INHA   
# data = db.execute("SELECT CustomerId , Country FROM Customers WHERE Country = 'USA' OR Country ='Canada'") # OR --> harvaqt yeki az tarafin True shavad 
# data = db.execute("SELECT CustomerId , Country FROM Customers WHERE NOt(Country = 'USA' OR Country ='Canada')") # OR
data = db.execute("SELECT CustomerId , Country FROM Customers WHERE Country = 'USA' AND CustomerId %2 = 0") # OR

for row in data:
    print(f"id ---> {row}")