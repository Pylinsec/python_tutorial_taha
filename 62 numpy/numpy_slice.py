import numpy as np
#  slicing --> ya heman tike tike kardadn ya cut kardan 
a = range(10)
arr = np.array(a)
# print(arr)
# print(len(arr))
# print(arr.ndim)
# print(type(arr))
# print(arr[1:5:2])
# print(arr[-5:-3])
# ------------------------------------------------------------------------
# array 2-D array
arr = np.array([[1,2,3],[4,5,7],[7,8,9,],[10,11,12],[13,14,15]])
# print(arr)
# print(arr.ndim)
# arr[start:end:step,start:end:step]
# print(arr[1:2])
# print(arr[1:3,:])
# print(arr[1:3,-1:])

# _________________________-------------------------------_________________________________
# -------------------------_______ 3-D array_____________---------------------------------

# arr[s:e:step,s:e:step,s:e:step]
arr_3 = np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]],[[13,14],[15,16],[17,18]]])
# print(arr_3)
# print(arr_3.ndim)
# print(arr_3[:,1:3,1:])
# print(arr_3[:,:,-2:-1])
print(arr_3.shape)


# 4-D array
# arr[s:e:step,s:e:step,s:e:step,s:e:step]
arr_4 = np.array([[[[1,2,3,4],[5,6,7,8]],
                   [[9,10,11,12],[13,14,15,16]],
                   [[17,18,19,20],[21,22,23,24]]],
                  [[[25,26,27,28],[29,30,31,32]],
                   [[33,34,35,36],[37,38,39,40]],
                   [[41,42,43,44],[45,46,47,48]]]])

print(arr_4)
print(arr_4.shape)