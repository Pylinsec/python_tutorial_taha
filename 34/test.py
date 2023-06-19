import sqlite3 , csv

db = sqlite3.connect("test.db")
# db.execute(f"CREATE TABLE post(postal TEXT , country  TEXT)")
with open("Book1.csv",'r') as file:
    reader = list(csv.reader(file))
    
    for i in range (1,len(reader)):
        print(i , reader[i])
        db.execute(f""" INSERT INTO post(postal , country) VALUES('{reader[i][0]}','{reader[i][1]}')""")
    db.commit()    