class Animal(object):
    def bark(self):
        print("---Animal---")


class Cat(Animal):
    def bark(self):
        print("---Cat---")


class Dog(Animal):
    def bark(self):
        print("---Dog---")


class SmallDog(Dog):
    def bark(self):
        print("---Small Dog---")


class Robot(object):
    def bark(self):
        print("---Robot---")


def animalBark(obj):
    obj.bark()


if __name__ == "__main__":
    cat = Cat()
    dog = Dog()
    sdog = SmallDog()
    robot = Robot()

    animalBark(cat)
    animalBark(dog)
    animalBark(sdog)
    animalBark(robot)
