text ="this is a pythoncoursefrom iran and i am teacherteacherhavijroobah for thiscourse."
list = text.split(" ")
print(list)
maxlen=0
for i in list:
    if maxlen < len(i):
        maxlen = len(i)
        temp = i

print(temp)


