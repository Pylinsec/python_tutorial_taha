import sqlite3

db = sqlite3.connect("kala.db")
table_row =db.execute("SELECT name FROM sqlite_master")
table_list = []
for row in table_row:
    print(row[0])
    table_list.append(row[0])
if "kharidar" not in table_list:
    db.execute("CREATE TABLE kharidar(name TEXT, lname TEXT, id INTEGER, phonenum TEXT)")    

db.execute("INSERT INTO kharidar (name , lname,id , phonenum) VALUES ('taha','nemati',1,'09')")
db.commit()