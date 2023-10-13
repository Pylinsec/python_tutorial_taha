def iter_test(iterable ,func):
    iterator1 = iter(iterable)
    
    try:
        while True:
            result = next(iterator1)
            func(result)
    except StopIteration:
        print("StopIteration")

iter_test([4.4,5,True,"python"],print)  