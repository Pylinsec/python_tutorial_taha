import csv


class MakeFile:
    def __init__(self):
        pass


    def makecsv(self):
        with open('file.csv','w' , newline='') as f:
            writer = csv.writer(f ,delimiter=',')
            writer.writerow([('taha','nemati','nohom')])  # string
            writer.writerows([('taha','nemati','nohom')])

    def csvreader(self):
        with open('file.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            for line in reader:  # list barmigardand
                print(line[0])

    def dictwrite(self):
        filed = ['name','lname','paye','age']
        with open('file.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f,fieldnames=filed ,delimiter=',') # filednames --> sar sotoon
            writer.writeheader()  # sabt header
            writer.writerow({'name':'taha','lname':'nemati','paye':'nohom' , 'age': 14})
            writer.writerow({'name': 'qoli', 'lname': 'jafari', 'paye': 'shesshom', 'age': 10})
            writer.writerows([{'name': 'toofan', 'lname': 'havij', 'paye': 'shesshom', 'age': 10},
                              {'name': 'jafar', 'lname': 'golabi', 'paye': 'shesshom', 'age': 12},
                              {'name': 'ali', 'lname': 'ahmadi', 'paye': 'hashtom', 'age': 13}])
    def dictread(self):
        with open('file.csv', 'r') as f:
            reader = csv.DictReader(f) # inja interator beraye ma misazad
            for line in reader:
                print(line['name'] ,  line['lname'])


'''
    def make_txt(self):
        with open('1.txt','w') as f:
            f.write('python')
    def readfile(self):
        with open('1.txt', 'r') as f:
            print(f.read())
'''


a = MakeFile()
# a.readfile()
a.csvreader()

# delimiter --> haman jodakonnade ast agar nezarim besoorat pishfarz  ','  estefadeh mikonad
# writerow()--> yechizi ke iterator bashe
