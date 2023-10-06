import numpy as np

# copy vs view --> 
arr = np.array([1,2,3,4,5])
# print(arr)
# print(arr.ndim)
# print(arr.dtype)

arr_copy = arr.copy()
arr_view = arr.view()

# print(arr_copy)
# print(arr_view)

# tevavot 1 --. id --> ashareh be jaye dar ram dareh
# print('id orginal-->', id(arr))
# print('id copy --> ',id(arr_copy))
# print('id view --> ',id(arr_view))

# 2 --> chiz avaz konim
arr[2]= 33
# print(arr)
# print(arr_copy)
# print(arr_view)

# change view
arr_view[3]= 44
print(arr)
print(arr_view)
print(arr_copy)

# base()
print(arr.base)
print(arr_copy.base) # dar in halat 
print(arr_view.base)