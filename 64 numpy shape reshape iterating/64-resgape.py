import numpy as np
# reshape be noei view hast
# reshape 1D to 2D -->
# range(start,end, step) 
a = range(24)
arr = np.array(a)
# print(arr)
# print(arr.reshape(3,8))
# print(arr.reshape(4,6))
# print(arr.reshape(6,4))
# print(arr.reshape(2,12))

# reshape 2_d to 3-D
# print(arr.reshape(2,3,4))
# print(arr.reshape(3,2,4))
# print(arr.reshape(6,2,2))
# new = arr.reshape(8,3,1)
# print(new)
# print(new.base)
# print(arr.reshape(2,4,-1)) # -1 --> ma nemidionim chanta 
# print(arr.reshape(-1,3,2))
print(arr.reshape(-1,4,6))


