import sqlite3

db = sqlite3.connect("qoli.db")
table_name = db.execute("SELECT name FROM sqlite_master")
table_list =[]
for row in table_name:
    table_list.append(row[0])
if 'student_tb' not in table_list:
    db.execute("CREATE TABLE student_tb (name TEXT ,lname TEXT , age INTEGER)")
if 'teacheer_tb' not in table_list:
    db.execute("CREATE TABLE teacheer_tb (name TEXT ,lname TEXT ,id INTEGER)")
if 'class_tb' not in table_list:
    db.execute("CREATE TABLE class_tb(name TEXT ,paye TEXT ,id INTEGER)")
if 'amval_tb' not in table_list:
    db.execute("CREATE TABLE amval_tb(name TEXT ,class TEXT ,serial INTEGER)")

# serfan jehat AMOOZESH
# table_list = db.execute("SELECT name FROM sqlite_master")
# # for row in table_list:
# #     print(row[0])
# list_table_name=[]
# for row in table_list:
#     list_table_name.append(row[0])
# print(list_table_name )   