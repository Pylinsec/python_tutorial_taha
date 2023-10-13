import numpy as np

# 1-D --> conctenate --> chaspandan yek arraye be tehe array dige
arr1 = np.array([1,2,3,46])
arr2 = np.array([4,5,6])
arr3 = np.concatenate((arr1,arr2))
# print(arr1)
# print(arr2)
print(arr3.ndim)
print(arr3)

# 2-D
a = np.array([[1,2],
              [3,4],
              [5,6]])
b = np.array([[11,22],
              [33,44],
              [55,66]])
# print(a.ndim)
# print(b.shape)
# axis=0
c = np.concatenate((a,a,a),axis=0)
print(c)
# axis =1
c = np.concatenate((a,b,a,b),axis=1)
print(c)

