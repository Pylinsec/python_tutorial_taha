import sqlite3

#  order by --> 
db = sqlite3.connect("chinook.db")
# format--> SELECT col1 ,col2 ,... FROM table_name WHERE condition  ORDER BY col1 , col2  ,... ASC/DESC
#  DESC --> DESCENDING -- NOOZOOLI 
#  ASC --> ASCINDING --> SUDOI  --> pishfarz ham hast 
# data = db.execute("SELECT FirstName FROM customers ORDER BY CustomerId DESC")
# data = db.execute("SELECT FirstName FROM customers ORDER BY FirstName DESC")
data = db.execute("SELECT FirstName , LastName FROM customers ORDER BY FirstName , LastName")
for row in data:
    print(row)
