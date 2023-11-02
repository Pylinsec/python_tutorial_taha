import numpy as np

arr1 = np.array(range(24)) # sakht arr 1-d
arr2 = np.reshape(arr1,(4,6)) # sakht arr 2-d
new = np.array_split(arr2,3,axis=0)
# print(new)
new = np.array_split(arr2,3,axis=1)
# print(arr2)
# print(new)


# ============hsplit heman array-split with axis=1
# print(np.hsplit(arr2,3))
# np.hsplit(arr,2) = np.array_split(arr,2,axis=1)

# vsplit heman array_split with axis=0
arr2 = np.reshape(arr1,(4,6)) 
print(arr2)
new = np.array_split(arr2,4,axis=0)
print(new)
print(np.vsplit(arr2,4))