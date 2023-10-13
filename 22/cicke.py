list1 = [1,2,3,4]

def test():
    while list1:
        for i in list1:
            yield i

while True:
    for i in list1:
        print(i)