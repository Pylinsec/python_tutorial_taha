import sqlite3
qoli = sqlite3.connect("qoli.db")
qoli.execute("CREATE TABLE if not exists cars(name TEXT, compani TEXT)")
column_list = []
data = qoli.execute("PRAGMA table_list")# Pragma ertebat dare ba memari database
for row in data:
    column_list.append(row[1])
# if 'model' not in column_list:
#     qoli.execute("ALTER TABLE cars ADD COLUMN model INT")
print(column_list)    