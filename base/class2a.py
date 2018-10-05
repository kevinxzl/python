class Animal(object):
    
    def __init__(self, name='Animal', color='white'):
        print("Animal:__init__")
        self._name = name
        self._color = color
        self._age = 8

    def __del__(self):
        print("Animal:__del__")

class Dog(Animal):
    def __init__(self):
        print("---Dog---")
        super().__init__()

   
    def __del__(self):
        print("Dog:__del__")

    def printinfo(self):
        self._color = "Yellow"
        print("name=%s, color=%s, age=%d" %(self._name, self._color, self._age))    

wc = Dog()
wc._name = "Tu Gou"
wc.printinfo()
