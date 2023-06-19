from re import L
import sqlite3
import os
db = sqlite3.connect('school.db')
#  os.remove()
# os.remove('school.db')  # hazf paygah dadeh 

# db.execute('CREATE TABLE hashtom(id INTEGER PRIMARY KEY,name TEXT,lname TEXT)') # sakht jadval 
# db.execute('ALTER TABLE hashtom RENAME TO haftom') # raname jadval 
# db.execute('DROP TABLE hashtom')  # hazf jadval 
# db.execute('ALTER TABLE haftom ADD COLUMN age INTEGER')  # azafeh kardan sootoon jadid be jadval

# make new table for teacher 
# db.execute('ALTER TABLE teacher DROP COLUMN NAME') # hazf sootoon az jadval 
# db.execute('ALTER TABLE teacher RENAME COLUMN lname TO lastname') # rename sootoon 


# db.execute("INSERT INTO haftom(name,lname , age) VALUES('havij','levashak',15)")
# db.execute("INSERT INTO haftom(name,lname , age) VALUES('torobdhe','toamto',15)")
# db.execute("INSERT INTO haftom(name,lname , age) VALUES('bolbol','boobaloo',15)")
# db.execute("INSERT INTO haftom(name,lname , age) VALUES('boz','goraz',15)")
# db.execute("INSERT INTO haftom(name,lname , age) VALUES('eagle','fil',15)")
# db.commit()
# db.execute("DELETE FROM haftom")  # HAZF KOL DATA HA 
# db.commit()
data = db.execute("SELECT name FROM haftom")
for item in data:
    # print(f" id = {item[0]} , name={item[1]}")
    print(item)