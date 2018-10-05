class Animal(object):
    
    def __init__(self, name='Animal', color='white'):
        print("Animal:__init__")
        self.name = name
        self.color = color
        self.age = 8

    def __del__(self):
        print("Animal:__del__")

class Dog(Animal):
   
    def __del__(self):
        print("Dog:__del__")

    def printinfo(self):
        print("name=%s, color=%s, age=%d" %(self.name, self.color, self.age))    

wc = Dog(name="Wang Cai")
wc.printinfo()
