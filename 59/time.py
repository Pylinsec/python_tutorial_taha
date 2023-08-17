import time

print(time.time())
t = time.gmtime(397)

print(time.strftime('%M:%S',t))