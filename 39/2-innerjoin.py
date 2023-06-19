import sqlite3
db = sqlite3.connect('alias.db')
#  inner join = join  --> zarb dekarti anjam midehad
# # left join = left outter join --> alave bar record haye ke meqdar anha dar sootoon moshterak berabar hast miare az jacval samt chap ham harche record hast miare  
data = db.execute("""
SELECT j.name ,q.name, q.telephone FROM qoli As q JOIN jafar As j ON q.name = j.name
""")
#  INNER JOIN (JOIN)--> hassas be sootoon moshtrak hast 
data = db.execute("""
SELECT * FROM jafar As j LEFT JOIN qoli As q ON q.name = j.name
""")
i = 1
for row in data:
    print(f"{i}-->{row}")
    i +=1