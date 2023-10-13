# str = "python"
# str1 = "tahahqxxx"
# print(str,end="\r") # carriage return  cursor barmigardanad aval satr 
# print(str1)
# _______________________________________________
# format 
str = 23.21
# print("{:04d}".format(str)) # digit ya integer 
# print("{:4.04f}".format(str)) # float 
# print("{:05s}".format(126)) # string 
#___________________________________________
# a,b,c,d=(1,2,4,4)
# print(a,b,c,d)

import time
def timer(t):
    try:
        while t:
            
            mins , seconds = divmod(t,60)
            # mins = t // 60
            # seconds = t % 60
            # print(f"0{mins}:{seconds}")
            print("{:02d}:{:02d}".format(mins,seconds),end="\r")
            
            time.sleep(1)
            t -= 1
            
        print("ok finish")
    except:
        pass  
t = int(input("inser seconds : "))
timer(t)      