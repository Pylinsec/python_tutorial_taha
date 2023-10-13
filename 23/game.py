import random
temp = []
for i in range(100):
    temp.append(100)
for i in range(100):
    random_num1 = random.randrange(0,99)
    temp[random_num1] -= 1
    for i in range(0,99):
        if temp[i] != temp[random_num1]:
            temp[i] += 1
        else:
            continue 
#     random_num2 = random.randrange(0,99)
#     while True:
#         if random_num2 != random_num1:
#             break
#         else:
#             random_num2 = random.randrange(0,99)
#     temp[random_num2] += 1
#     print(random_num2,temp[random_num2])
temp.sort()
print(temp)
