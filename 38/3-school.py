import sqlite3
# MIN ,MAX, SUM  , AVG --> FEGHAT DADEHAYE ADADI
# COUNT --> HARCHIZI 
db = sqlite3.connect('school.db')
data = db.execute("SELECT MIN(score) FROM dars") # MIN DEDYHAYE SOOTOON
data = db.execute("SELECT MAX(score) FROM dars") # MAX DADEHAYE SOOTOON
data = db.execute("SELECT SUM(score) FROM dars") # MAJMOO TEMAM DADEHAYE SOOTOON
data = db.execute("SELECT COUNT(score) FROM dars WHERE score < 10 ") # SHOMARESH YA TEDAD REDIF HA 
data = db.execute("SELECT AVG(score) FROM dars WHERE score <10 ") # 
data = db.execute("SELECT COUNT(name) FROM dars WHERE score  >10 ") # 
data = db.execute("SELECT DISTINCT SCORE  FROM dars ") # TEKRAR HAZF SHEVAD
data = db.execute("SELECT id,score  FROM dars WHERE score IS NULL ") # harja null hast biar 
# data = db.execute("SELECT name ,score  FROM dars WHERE score IS NOT NULL ") # harja ke null nist bia 

for row in data:
    print(row)