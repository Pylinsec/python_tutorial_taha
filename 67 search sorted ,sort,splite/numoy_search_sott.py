import numpy as np 


# search sorted  --> np,.searchsorted(arr,value)
arr1 = np.array([22,4,1,22,5,6,4,30,4])
x = np.searchsorted(arr1,4)
# print(np.sort(arr1))  # sort item haye arraye anjam mide 
# print(x) # --> akharin index ke ba value match hast miareh 

# ======================================================================
# side ='left' --> DEFAULT , side ='right' 
arr1 = np.array([21,22,23,26])
print(np.sort(arr1))
# x = np.searchsorted(arr1,23)
# print(x)
x = np.searchsorted(arr1,24,side='left')
print(x)
x = np.searchsorted(arr1,24,side='right')
print(x)