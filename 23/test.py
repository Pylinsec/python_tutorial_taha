import time
def inc(counter):
    time.sleep(1)
    print(counter)
    inc(counter- 1)

inc(100)    