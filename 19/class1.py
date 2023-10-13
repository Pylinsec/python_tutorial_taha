class Animal:
    def __init__(self,type):
        self.type = type
        print(self.type)

    def tekan(self):
        print ("\\-//--\\")  

    


class Cat(Animal):
    def __init__(self, name_cat , type):
        super().__init__(type)
        self.name_cat = name_cat
        print(self.name_cat)
 
    def miomio(self):
        print("miomio")

# dog = Animal    
# dog("charlea").tekan()     
# dog("charlea").miomio()     
 
# tommy = Cat
# tommy("tommy","hairy").tekan()
