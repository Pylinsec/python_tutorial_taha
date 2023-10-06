import numpy as np

a =range(24)

# iteratin in 1-D
arr = np.array(a,ndmin=1)
# print(arr)
# for item in arr:
#     print(item,end=' ')

# iteratin in 2-D
arr = arr.reshape(3,8)
# for x in arr:
#     for y in x:
#         print(y,end=' ')

arr = arr.reshape(2,2,2,3)
print(arr)
for x in np.nditer(arr):
    print(x)