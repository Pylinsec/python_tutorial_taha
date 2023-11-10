import numpy as np

a = np.array(range(12))
# print(a)
# append()_> azafeh kardan item be tahe array
# print(np.append(array,23)) --> format
# print(np.append(a,23)) 
# print(np.append(a,(34,23,23)))
# print(np.append(a,[34,23,23]))
# print(np.append(a,{34,23,23}))

# =============================================================================
# insert(array,index,value,axis)
# b= a.reshape((2,6))
# print(b)
# c = np.insert(b,3,1500)
# print(np.insert(b,3,1500))

# =========================================
# np.delete(array,index,axis)
# print(b)
# print(np.delete(b,(1,2,3,4))) 
# print(np.delete(b,3,axis=1)) # dar har radif index 3 ra hazf mikonad 

# resize() , reshape()
print(a)
c = a.reshape((3,4))
d = np.resize(a,(3,4))
print(c)
print(d)

print(c.base,d.base)