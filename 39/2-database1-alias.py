import sqlite3
db = sqlite3.connect('alias.db')
data = db.execute("""
SELECT j.job ,q.telephone FROM jafar As j , qoli As q WHERE j.name = q.name
""")
for row in data:
    print(row)
#  Alias --> dadan name mostear be table ha v column ha 
