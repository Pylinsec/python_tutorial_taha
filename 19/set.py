#difination  
#unchangable   bad az sakht digar nimishavad on ra tagiir dad
# unorderd  qanooni berash nist ke kodam item aval biad 
set1 = {78 , "python",4.5, True}
print(set1)
# for i in set1:
#     print(i,end=" ")
 #not allow duplicate   ozve tekrari hazf mikonad
set2 = {1,2,3,1,2,4,55,6}
# print(len(set2))    
# print(set2)
# print( 8 in set1)

# constructor  set (list ,string ,tuple )
# list1 = [1,24,4]
# print(type(list1))
# set4 = set(list1) 
# print(type(set1))
# ___________________________________
#add items  set.add(item)    set1.update(set2)  set1 ,set2 dar set1 mirizad
set1.add("levashak")
print(set1)
set1.update(set2)
print(set1)
#remove clear discard del
# set2.remove(55)  # AGAR ADDAD BOOD HAZF MIKONAD AGAR NEBOOD ERROR MIDEHAD 
# print(set2)
set2.discard(555) # AGAR ADDAD BOOD HAZF MIKONAD AGAR NEBOOD ERROR nemidehad
print(set2)
set2.clear() # hazf itemhay dakhel set 
print(set2)

# del set2  # khod sakhteman dadeh ra hazf konid 
# print(set2)

#union or update -intersection ,intersection_update - symetric_deffrence , symetric_deffrence_update 
set1.union(set2) # hamey ozvhaye 2 set mirizad dakhel set1
set1.update(set2)

set1.intersection(set2)  # ozvhaye moshtrak 
set1 = {1,2,4,5,4}
set2 = {11,2,4,25,4}
# z = set1.intersection(set2)  # dar in halat bayad dar var sevoom rikhteh shevad 
# set1.intersection_update(set2)  # khod set1 ra update mikonad 
# print(z)
# print(set1)

set3 = set1.symmetric_difference(set2)  # ozvhaye moshtrak ra hazf mikonad va baqye ra miavrad 
set1.symmetric_difference_update(set2)
print(set3)
print(set1)
