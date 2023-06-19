import sqlite3
class Car:
    def __init__(self):
        self.db = sqlite3.connect("car.db")
        # self.db = self.db.cursor() # mekan nema
        self.make_table()

    def make_table(self):
        self.db.execute("""
        CREATE TABLE if not exists 
        car(id INT PRIMARY KEY,name TEXT , year INT,country TEXT,color TEXT)
        
        """)

    def add_row(self):
        self.db.execute("""
        INSERT INTO car VALUES(2,'pride',1395,'iran','white')
        """)
        self.db.execute("""
        INSERT INTO car VALUES(3,'x33',1385,'china','green')
        """)
        self.db.execute("""
        INSERT INTO car VALUES(4,'ford',1305,'usa','black')
        """)
        self.db.execute("""
        INSERT INTO car VALUES(5,'pegout',1285,'france','blue')
        """)
        self.db.execute("""
        INSERT INTO car VALUES(6,'bmw',1495,'germani','red')
        """)
        self.db.commit()

    def show_data(self):
        data = self.db.execute("SELECT * FROM car")
        for name in data.description:
            print(name[0] , end="  ")
        print()    
        for row in data:
            print(row[0],row[1],row[2],row[3],row[4])

    # data update in database 
    # hoshadar--> hatman hengam estefadeh az delete v update az where estefadeh shevad
    def update_database(self):
        self.db.execute("UPDATE car SET name='reno', year=1800 WHERE  country='iran'")
        self.db.commit()

    def delete_from(self):
        self.db.execute("DELETE FROM car WHERE country='iran'")
        self.db.commit()
c = Car
c().delete_from()