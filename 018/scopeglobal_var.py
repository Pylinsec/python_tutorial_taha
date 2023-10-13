
# globla  hameja qabel dastresi hast
x=454
#scope  feqat dakhel heman tabe megar inke on ra global konim
def scope_test():
    z = "scope"
    global x
    x = 345
    global y
    y = 500
    print(f"{x} is varible inside function")
def global_test():
    print (x + 1000)
    print (y)
scope_test()
global_test()
   
