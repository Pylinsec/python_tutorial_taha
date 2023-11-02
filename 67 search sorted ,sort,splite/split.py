import numpy as np 

# split
arr = np.array(range(24))
# print(arr,arr.shape,arr.ndim,arr.base,arr.dtype,arr.size)
# ====================================================================================
# array split 1-D  --> np.array_split(arr,adad) --> addad tedad array hast 
new = np.array_split(arr,8) # sakht list az arraye ke 8 ta arraye misaze 
# print(new)
new = np.array_split(arr,6)
# print(new)
new = np.array_split(arr,10)
# print(new[1].base) 
# print(new)

# =============================2-D array split=========================================
arr2 = np.reshape(arr,(4,6))
print(arr2)
print(np.array_split(arr2,3))
print(np.array_split(arr2,2))