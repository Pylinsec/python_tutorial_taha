# list []] changeable , oredrd , duplicate 
#dictionary {x:y}  changeable , orderd , no duplicate member
# tuple (x,y,z)    unchangeable , orderd , duplicate
# set {}  unorderd , no duplicate,unchangable

print((((len((1 ,1,1.3,False,"tuple"))))))
havij = (1 ,1,1.3,False,"tuple")
#test duplicate
print(havij)
#test orderd 
print((1 ,1,1.3,False,"tuple") == (1 ,1.3,1,False,"tuple")) 
"""test un changeable tuple = ("python",)  # vajeb eini hast 
ke beraye temayoz tuple , string , gozashte shevvad"""
# string= ("string")
# print (type(tuple),type(string))
# havij2 = (1 ,4,1.3,False,"tuple")
# print(havij2[1:3])
# print(havij2[-4:-1])


# for i in havij2:
#     print(i)
# print(4 in havij2)    
# print(4 not in havij2)  
# havij2 = [1 ,4,1.3,False,"tuple"]
# havij3 = [str(i) + "tr" for i in havij2 ] # list comperehension 
# list2= [ i **2 for i in range (10) if i %2 == 1 ]
# print(havij3)
# print(list2)


# change tuple 
havij1 = (1 ,1,1.3,False,"tuple") 
havij3 = list(havij1)
havij3[4]= "pofak"
havij3.append("levashak")
print(type(havij3))
havij1 = tuple(havij3)
print(type(havij1))
print(havij1)

# method join , count , index
print(havij1.count(1))
tup1 = (1,2,"palang")
tup2 = (1,2,"goraz")
tup3 = tup1 + tup2
tup4 = tup3 * 3  # tup3 3 bar mineviseh
print(tup3)
print(tup4)
print(tup1.index("palang"))