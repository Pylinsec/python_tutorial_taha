def test(x):
    for i in range(x):
        return i
    return x + 2
    return x + 2
    return x + 2
test(5)

#generator  yek neshane darad on ham yield
# tefavot tabe mamolloi ba generator
# aval tabe return darad  vali generator yield darad
# 
# def test(x):
    
#     yield x + 1
#     yield x + 2
#     yield x + 3
#     yield x + 4
# print(tuple(test(4)))
# print(list(test(4)))
# print(set(test(4)))
# print(dict(zip(test(4),test(5)))) # zip 2 ta itrable  migirad va dictionary pass midehad


def counter(x):
    for i in range(x):
        print(i)
        yield(i)

for k in counter(20000):        
    print(f"out:{k}")

