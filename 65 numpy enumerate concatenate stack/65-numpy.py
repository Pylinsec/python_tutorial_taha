import numpy as np 

# jehat mooroor gozashteh -----------------------------------------------------
li = [1,2,4,5,5,6]
for index , item in enumerate(li):
    # print(index, item)
    pass

# D-1 ---- np.ndenumerate(arr) -----------------------------------------------------
a = range(12)
arr = np.array(a)
for index , item in np.ndenumerate(arr):
    # print(f"{index}-->{item}")# index besoorat tuple hast
    pass


# 2-D --> np.ndenumerate(arr) *****************************************************************

arr = np.array(range(1,25))
new = arr.reshape(4,6)
print(new)
for x,y in np.ndenumerate(new):
    # print(f"{x}--> {y}")
    pass

#3_D np.ndenumerate(arr) **********************************
new3 = arr.reshape(2,3,4)
for index , item in np.ndenumerate(new3):
    print(f"{index}-->{item}")