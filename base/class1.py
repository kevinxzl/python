#encoding=utf-8
class Dog:
    def __init__(self, name, weight, color, age):
        self.name = name
        self.weight = weight
        self.color = color
        self.__age = age

    def __str__(self):
        return self.name + " " + str(self.weight) + " " + self.color + " " + str(self.__age)
    
    def getInfo(self):
        return self.name, self.weight, self.color

    def bark(self):
        print("Wang Wang.....")

    def run(self):
        print("Dog is running....")
        self.weight -= 2

    def eat(self):
        print("Dog is eating....")
        self.weight += 5

if __name__ == "__main__":
    dog1 = Dog("JingMao", 20, "Yellow", 3)
    print(dog1)
    print("dog1 addr:", id(dog1))
    print("Dog Info:", dog1.getInfo())
    dog1.bark()
    dog1.run()
    dog1.color = "White"
    dog1.eat()
    print("Dog Info", dog1.getInfo())