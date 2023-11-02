import numpy as np
# where --> tuple 
arr1 = np.array([22,1,4,5,6,4,30,4])
# np.where(condition shart)
x = np.where(arr1==4) # bargardandn index harja ke value 4 basshe
print(x)

x = np.where(arr1 > 20)
print(x)

x = np.where(arr1 % 2 == 0)
print(x)

# np.where in 2-D
arr2 = np.array([[1,2,3,4],[2,7,3,8]])
x = np.where(arr2 > 3)
print(x)

# output--> (array([0, 1, 1], dtype=int64), array([3, 1, 3], dtype=int64)) -->(0,3),(1,1),(1,3)

# np.where in 3-D
arr3 = np.array([[[2,3,4],
                  [5,0,1]],
                 [[-1,-4,0],
                  [4,60,9]]])
x = np.where(arr3 == 0)
print(x)