import sqlite3

# CREATE , ALTER  ..RENAME TO , DROP

# make database with sqlite3.connect
try:
    db = sqlite3.connect('customer.db') # agar customer bood ke vasl mishe agar nebood misaze v vasel miseh
    # # make table in db
    # db.execute("CREATE TABLE kala(id INTEGER PRIMARY KEY,name TEXT , lname TEXT , age INTEGER)")
    # db.execute('CREATE TABLE frooshandeh(name TEXT , lname TEXT , mobile INTEGER)')
    # db.commit() #gereftan taeidieh
    # db.execute("DROP TABLE frooshandeh") # DROP TABLE  hazf table
    db.execute('ALTER TABLE kala RENAME TO golabi')  # ALTER TABLE name RENAME TO new name   --> tageir name table

except:
    print('ERROR')

