import numpy as np

# dtype ya datatype
arr = np.array([1,2,3])
print(arr.dtype) #int32
arr = np.array([1.2,2.3,4.5])
print(arr.dtype) # float64
arr = np.array([True,False,False])
print(arr.dtype) #bool

# define type --> dtype=
arr = np.array([1,2,4],dtype='U') # U --> string , i --> int , f --> float , b--> boolean
print(arr)

#  test konim
# arr = np.array(['a','b'],dtype='i') error mide
arr = np.array(['3','5'],dtype='i') # agar ham no bashand tabdil mishe
arr = np.array(['3','5'],dtype='f')# agar ham no bashand tabdil mishe
arr = np.array([True,False],dtype='i')
arr = np.array([1,2,3,4,0,True],dtype='b')
print(arr)
