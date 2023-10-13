class Dog:
    #state or attribute
    name= "teddy"
    age = 4
    color= "white"
    #method or behavior
    def eat(self):
        print("dog eat bone")
    def bark(self):
        print("dog is barked ")

teddy = Dog()
cat = Dog()
print(teddy.name);print(teddy.age);print(teddy.color)
cat.eat()
cat.bark()

