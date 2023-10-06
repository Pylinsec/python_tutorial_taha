import numpy as np

# 1-D arr
arr = np.array([1,2,3])
# print(arr.shape)

# 2-D arr
# shape --> (m,n) --> m--> tedad radif ,n tedad sootoon
arr = np.array([[1,2],
                [3,4],
                [5,6]])
# print(arr.shape)
# print(arr)

# 3_D --> (k,m,n) --> k ta array 2_d ba shape (m,n)
arr = np.array([[[1,2,6],
                 [3,4,7],
                 [11,22,33]],
                [[5,6,8],
                 [7,8,9],
                 [14,15,16]]])
# print(arr.shape)

# 4-D shape (u,k,m,n) --> U --> tedad 3 D , k --> tedad 2 D dar har 3D 

# ndmin --> hadaqal nd
arr = np.array([[[1,2,6],
                 [3,4,7],
                 [11,22,33]],
                [[5,6,8],
                 [7,8,9],
                 [14,15,16]]],ndmin=10)

print(arr.shape)
print(arr)