import csv
import sqlite3

def read_sql():
    db = sqlite3.connect('chinook.db')
    data = db.execute("""
    SELECT * FROM customers limit 20
    """)

    #  for name column 
    column_name = []#  for make list for data of tuple from database 
    data_list =[]
    for name_col in data.description:
        column_name.append(name_col[0])

    for row in data:
        data_list.append(row)  
    print('make datalist is successfully')          
    make_csv(column_name , data_list)    
    
#  write data in csv file 
def make_csv(columnname , datalist):
    with open('customer.csv','w' ,encoding='utf-8',newline='') as file: 
        writer = csv.writer(file)
        writer.writerow(columnname)
        writer.writerows(datalist)


read_sql()        