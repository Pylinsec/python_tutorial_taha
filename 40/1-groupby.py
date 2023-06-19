import sqlite3

# WHERE condtition  --> GROUP BY column --> ORDER BY column 

#  table name from chinook
'''
albums   sqlite_sequence   artists  customers
employees  genres  invoices  invoice_items
media_types   playlists  playlist_track
'''
db = sqlite3.connect('chinook.db')
# yadavari
# tables = db.execute("SELECT * FROM sqlite_master")
# for table in tables:
#     print(table[1])

data = db.execute("SELECT count(country) As cc,country FROM customers GROUP BY country ORDER BY cc DESC ")
data = db.execute("SELECT count(country) As cc,count(FirstName),country, FirstName FROM customers GROUP BY FirstName ORDER BY cc DESC ")
data = db.execute("SELECT country FROM customers GROUP BY country ")
data = db.execute("SELECT FirstName FROM customers GROUP BY country ")
for row in data:
    print(f"{row}")