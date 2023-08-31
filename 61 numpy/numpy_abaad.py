import numpy as np


# 0-d array 
arr = np.array(45)
# print(type(arr))
# print(arr, arr.ndim) # ndim --> level array 

# 1_d array  --> dimensional yani boed ابعاد یا بعد 
arr = np.array([1,2,3,4,5])
# print(arr)
# print(arr.ndim)

# 2_d array
arr = np.array([[1,2],[3,4]])
# print(arr)
# print(arr.ndim)

# 3_d array
arr = np.array([[[1,2],[11,23]],[[2,4],[445,6]]])
print(arr)
print(arr.ndim)

# n_d array 
arr = np.array([1,2,3,4,5,6,7],ndmin=6)
print(arr[0,0,0,0,0])
print(arr)

