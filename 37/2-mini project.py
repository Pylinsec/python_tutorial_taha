import sqlite3
#  print table and column 

db = sqlite3.connect("chinook.db")
data_table = db.execute("PRAGMA table_list")
table_list_name =[]

for row in data_table:
    table_list_name.append(row[1])
    
newlist = table_list_name[1:len(table_list_name)-1]
print(newlist)

for name in newlist:
    temp =[]
    table_details = db.execute(f"PRAGMA table_info({name})")
    for row in table_details:
        temp.append(row[1])
    print(f"{name}  ****--->{tuple(temp)}")

