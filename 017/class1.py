class Animal:
    def __init__(self ,name):  # init  heman initial be mani shoro ya start
        print(name , "bedone self")
        print(name ," is animal")
        self.name = name
        
    def printA(self):
        print(self.name,"print form printA")
        
        
    def printB(self):
        print(self.name,"print form printB")
        
        
    def printC(self):
        print("print form printC")
        
        
class Dog:
    def __init__(self , name , color , domestic):
        self.name = name
        self.color = color
        self.domestic = domestic
    def none_cant_fly(self):
        print(self.name , "cant fly ")
        
    def animal_can_swim(self):
        print(f"color of {self.name} is {self.color} and {self.name} can swimm")
        
    def is_domestic(self):
        if self.domestic:
            print(f"{self.name} is domestic animal")
        else:
            print(f"{self.name} is wild animal")
        
charli = Dog("charli","yellow",True)
charli.animal_can_swim()
max = Dog("max","white",True)
max.is_domestic()
wolf = Dog("wolf","gray",False)
wolf.is_domestic()
        
        

# dog = Animal("dog")
# dog.printC()

        


def printA(name):
    print("print form printA")
def printB(name):
    print("print form printB")
def printC(name):
    print(name,"print form printC")


