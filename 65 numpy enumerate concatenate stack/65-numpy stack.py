import numpy as np

# 1-D --> stack --> arrye 2-d mishe
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

c = np.stack((a,b),axis=0)
# print(a.ndim ,c.ndim)
print('stack with axis=0\n',c)
c = np.stack((a,b),axis=1)
print('stack with axis=1\n',c)

# hstack --> horizontal --> ofoqi --> heman concatenate hast
print('hstack\n',np.hstack((a,b)))

# vstack --> vertical amoodi
print('vstack\n',np.vstack((a,b)))  # heman np.staci((a,b),axis=0)

# dstack --> depth amoodi
print('dstack\n',np.dstack((a,b)))  # heman np.staci((a,b),axis=0)