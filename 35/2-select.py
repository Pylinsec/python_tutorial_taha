import sqlite3

chinook = sqlite3.connect("chinook.db")
table_list = chinook.execute("SELECT * FROM SQLITE_MASTER" )
for row in table_list:
    print(row)