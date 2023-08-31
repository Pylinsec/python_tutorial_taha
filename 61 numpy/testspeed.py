import numpy as np
import time

n = range(100000000)

li = list(n)
arr = np.array(n,dtype=np.float64)
sum = 0
#  arr time
def calc_l(b):
    t1 = time.time()
    sum = 0
    for i in b:
        sum += i
    return time.time() - t1    
print(calc_l(li))


#  list time
def calc_arr(a):
    t1 = time.time()
    sum = 0
    for i in a:
        sum += i
    return time.time() - t1    
print(calc_arr(arr))

# 