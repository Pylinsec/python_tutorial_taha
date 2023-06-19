import sqlite3

db = sqlite3.connect('taha.db')
data = db.execute("select * from etelaat")
for row in data:
    print(row)

db.execute("CREATE TABLE if not exists copy (newjob TEXT , newage INTEGER)")    
data = db.execute("INSERT INTO copy select job , age from etelaat")
db.commit()
