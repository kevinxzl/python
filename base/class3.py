class Animal(object):
    def __init__(self):
        self.a   = 1
        self._b  = 2
        self.__c = 3

    def test1(self):
        print("Animal:--public", self.a, self._b, self.__c)

    def _test2(self):
        print("Animal:--protected", self.a, self._b, self.__c)

    def __test3(self):
        print("Animal:--private", self.a, self._b, self.__c)


class Dog(Animal):
    def test1(self):
        print("Dog:-test1", self.a, self._b)

    def test2(self):
        print("Dog:-test2", self.a, self._b)
    
    def test3(self):
        print("Dog:-test3", self.__c)


if __name__ == "__main__":
    aa = Animal()
    aa.test1()
    aa._test2()
  #  aa.__test3()
    aa.a = 10
    aa._b = 20
    aa.__c = 30
    aa.test1()
  


    dd = Dog()
    dd.test1()
    dd.test2()
 #   dd.test3()
    dd.a = 100
    dd._b = 200
    dd.test1()
    dd.test2()


  #  dd.test2()
