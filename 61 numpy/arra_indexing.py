import numpy as np

# indexing for 0_d array
arr = np.array(34)
# print(arr) # dar in halat index khasi nemish tesavor kard 
# --------------------------------1-d---------------------------------------------
# indexing for 1_d array
arr = np.array([1,2,3,4,5])
# index mosbat
# print(arr[2])
# index manfi
# print(arr[-2])

# --------------------------------2-d-----------------------------------------------
# indexing 2_d array
arr = np.array([[1,2],[3,4]])
# index mosbat
# print(arr[1])
# print(arr[1][1])
# print(arr[1,1])
# # index manfi
# print(arr[-1,-1])

# -----------------------------------------3-d--------------------------------------------
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr)
print(arr[1,0,1])

# -----------------------------------------4-d--------------------------------------------
arr = np.array([[[[1]],[[4]]]])
print(arr)
# print(arr[1][1][0][0])
