#iter: ye tabe hast ke ye done itrable migire va on ra tabdil be itrator mikone 
#iterable: chizi ke ma tabe iter() ba saresh miarim , iterator  list tuple string dictionary set
#itrator : chizi hast  ke tabe next() bar saresh miad 
#iterable1 = [1,2,3,4,5]
#iterable1 = (1,2,3,4,5)
#iterable1 = {1,2,3,4,5}
# iterable1 = {1:2,3:4}
# iterator1 = iter("python")
# print(type(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))

def iter_test(iterable ,func):
    iterator1 = iter(iterable)
    
    try:
        while True:
            result = next(iterator1)
            print(result)
            func(result)
    except StopIteration:
        print("StopIteration")

iter_test([4.4,5,True,"python"],print)        
