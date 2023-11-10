import numpy as np 
# additin , subtraction ,multiplication,powoer or exponentiation,modulus or reminder or mod ,divivion,absolute
a1 = np.array([22,33,44,55])
a2 = np.array([3,4,5,6])

b1 = np.array([[1,2],[3,4]])
b2 = np.array([[11,22],[33,44]])
# jehat anjam amal riazo lazem hast ke size berabar bashad
print(np.add(a1,a2))
print(np.add(b1,b2))
# subtract yani tafriq
print(np.subtract(a1,a2))
print(np.subtract(a2,a1))

# multiply --> zarb
print(np.multiply(a1,a2))
# divide , taqsim
print(np.divide(a1,a2))
# divmod
print(np.divmod(a1,a2)) # 2ta array barmigardand avbali div hast dovomi mod ast

# mod or reminder or modulus
print(np.mod(a1,a2))
print(np.remainder(a1,a2))

# power
print(np.power(a1,a2)) 

# abs or absolute
a2 = np.array([3,-4,5,-6])
print(np.abs(a2))
print(np.absolute(a2))
print(np.negative(a2))