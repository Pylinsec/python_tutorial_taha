import datetime  # lazem nist ke kol ketabkhane ya module ya lib  hame ra belad bashid
import time

print(time.ctime(0)) # ekhtelf sanye az tarikh 1/1/1970 
print(dir(time))
# print(time.sleep(3))
# 
# for i in range (20,0,-1):
#     time.sleep(2) 
#     print(i,end=" ")
# today = datetime.datetime.now()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.hour)
# print(today.minute)
# print(today.second)

birthday = datetime.datetime(2008,6,9,20,15,15,656565)
print(birthday)
print(birthday.strftime("%A rooze %a sal %G saat %H"))