# decorator input on yek tabe ast , return ham tabe 
# karbord bishtar beraye test zeman ejraye 
#print("A" * 30) # zarb bad az string be manaye tekratr hast
import time

def star(func): # out function 
    def inner():  # inside function 
        print ("%" * 30)
        print ("*" * 30)
        starttime = time.time()
        func()  # input function  
        endtime = time.time()
        print(endtime -starttime)
        print ("%" * 30)
        print ("*" * 30)
    return inner  # inside function  

# input function 
def printer(): 
    sum = 0
    for i in range (100000000):
        sum += i
    return sum  

#revesh aval seda kardan deorator
star(printer)()




# # revesh 2
# @star  # dar in revesh tabe bayad zir tarif sheved 
# def printer():
#     print("python")  
# printer() 





# def add (a,*num):
#     sum = 0
#     for i in num:
#         sum = sum + i
#         print(a)
#     return sum
# e = add(2,35,5,5,5,5,6,7,7,9,5)
# print(e)