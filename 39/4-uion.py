import sqlite3
#  UNION OR UNION ALL ---> EJTEMA DO TA JADVAL 
'''
SHART:--> 
1-select ke mizenim bayad dar har do taraf union tedad mosavi bashad 
2-data type ha bayad yeki bashad 
3-order ASC DESC  --> bayad dar yek order bashand 

'''
db = sqlite3.connect('alias.db')
data = db.execute("""
SELECT name FROM jafar UNION ALL select name FROM qoli
""")
for row in data:
    print(row)