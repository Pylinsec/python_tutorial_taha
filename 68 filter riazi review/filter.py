import numpy as np 

arr = np.array([23,34,55,22,12,-98,100,877])
x = [True,False,True,True,False,False,False,True]
# print(arr[x])

# joda kardan item haye zoj az array
arr1 = np.array(range(50))
# print(arr1)

filter =[]
for item in arr1:
    if item % 2 == 0:
        filter.append(True)
    else:
        filter.append(False)  
print(filter)        
print(arr1[filter])          