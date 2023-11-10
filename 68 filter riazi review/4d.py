import numpy as np 

a1 = np.array(range(12))
a1 = np.resize(a1,(4,3))
print(a1)


a2 = np.arange(-20,-8,1)
a2 = a2.reshape((4,3))
print(a2)

print(np.abs(a2))
print(np.power(a2,a1))
