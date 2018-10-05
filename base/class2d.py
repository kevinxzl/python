class Animal(object):
    nameA = "Animal: nameA"
    _colorA= "Animal: colorA"
    __ageA = "Animal: ageA"

    def __init__(self, name='Animal', color='white'):
        print("Animal:__init__")
        self.name = name
        self.color = color
        self.age = 8

    def __del__(self):
        print("Animal:__del__")

    def printinfo(self):
        nameA = "TuGou"
        self.__ageA = "18"
        print("Animal-printinfo:", self.nameA,"|", self._colorA,"|", self.__ageA)
        print("name=%s, color=%s, age=%d" %(self.name, self.color, self.age)) 

class Dog(Animal):
    def __init__(self):
       print("Dog:__init__")

    def __del__(self):
        print("Dog:__del__")

    def printinfo(self):
       # self.nameA = "TuGou"
       # self._colorA = "RED"
       # self.__ageA = "18"
        #print("name=%s, color=%s, age=%d" %(self.name, self.color, self.age)) 
        #print("name=%s, color=%s, age=%s" %(self.nameA, self.colorA, self.ageA))   
        print("Dog:nameA=", self.nameA,"|","Dog:_colorA=", self._colorA, "|") 


#wc = Dog(name="Wang Cai")
print("Test Animal:")
anim = Animal()
anim.printinfo()

print("Test Dog:")
wc = Dog()
wc.nameA= "XiaoXiong"
wc._colorA = "Black"
wc.__ageA = "100"
wc.printinfo()

