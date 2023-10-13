print("golabi ")
# agar bekhahim dar dir qabltar file besazim az ../ be azaye har folde eqabter
# agar bekhahimn dar folder dar hamin masir file besazim bayad qabl an folder ra sakhteh bashim
with open ("sub/sub.txt","r") as file:
    for line in file.readlines():
        #print(line[:-1])  #revesh 1
        #print(line[:len(line)-1]) #revesh 2
        print(line.rstrip('\n'))  #revesh 3

