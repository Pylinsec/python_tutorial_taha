import sqlite3

# db = sqlite3.Connection("chinook.db")
# data = db.execute("PRAGMA table_list")
# for coul in data:
#     print(coul)
db = sqlite3.Connection("joojeh.db")
list_table = db.execute("PRAGMA table_list")
list_column = db.execute("PRAGMA table_info(hen)")
tb_list =[]
col_list=[]
for name in list_column:
    col_list.append(name[1])
for name in list_table:
    tb_list.append(name[1])
if "hen" not in tb_list:
    db.execute("CREATE TABLE hen(name TEXT, color TEXT)")
if 'age' not in col_list:
    db.execute("ALTER TABLE hen ADD COLUMN  age INTEGER")    
                          
