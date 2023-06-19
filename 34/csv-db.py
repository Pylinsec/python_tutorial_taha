import csv , sqlite3

class ReadToDb:
    def __init__(self):
        self.reader_csv()
        self.create_db()
        self.insert_data()
        # self.student_db.execute(f"""INSERT INTO data(Id,CustomerName
        #     ,ContactName,Address, City,PostalCode,Country) VALUES('2','sajjad','sajjad','tehran','abali','454','qatar')""")

        # for row in self.student_db.execute("SELECT * FROM data"):
        #     print(row)

    def create_db(self):
        self.student_db = sqlite3.connect("student.db") 
        # self.student_db.execute(f"""CREATE TABLE data ( {self.row0[0]} INT, {self.row0[1]} TEXT,
        # {self.row0[2]} TEXT, {self.row0[3]} TEXT ,{self.row0[4]} TEXT ,
        # {self.row0[5]} TEXT ,{self.row0[6]} TEXT)""")  

    def reader_csv(self):
        with open ("student.csv",'r' , encoding='utf-8-sig') as f:
            self.reader = list(csv.reader(f))
            self.row0 = self.reader[0]
            for row in self.reader:
                print(row)

    def insert_data(self):
        # for i in range(1,len(self.reader)):
        #     print(type(self.reader[i][0]))
        #     self.student_db.execute(f"""INSERT INTO data VALUES('{self.reader[i][0]}',
        #     '{self.reader[i][1]}',
        #     '{self.reader[i][2]}','{self.reader[i][3]}','{self.reader[i][4]}',
        #     '{self.reader[i][5]}','{self.reader[i][6]}')""")

        for i in range(1,len(self.reader)):
            print(self.row0[0])
            self.student_db.execute(f"""INSERT INTO data VALUES('{self.reader[i][0]}',
            '{self.reader[i][1]}','{self.reader[i][2]}','{self.reader[i][3]}','{self.reader[i][4]}',
            '{self.reader[i][5]}','{self.reader[i][6]}')""")
            self.student_db.commit()
        

            
                
            

ReadToDb()            