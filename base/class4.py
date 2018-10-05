class A(object):
    def __init__(self):
        self.a1 = "A:a1"
        self.a2 = "A:a2"

    def test(self):
        print("----A---Test")
    
    def testA(self):
        print("----A-----TestA")

class B(A):
    def __init__(self):
        self.b1 = "B:b1"
        self.a2 = "B:a2"

    def test(self):
        print("B-Test---B---Test")
        print("B-Test", self.a1, self.a2, self.b1)
    
    def testB(self):
        print("---B---TestB")

class C(A):
    def __init__(self):
        self.c1 = "C:c1"
        self.a2 = "C:a2"
    def test(self):
        print("----C----Test")
    
    def testC(self):
        print("------C-----TestC")

class D(B, C):
    def __init__(self):
        self.d1 = "D:d1"
        self.a2 = "D:a2"
    def test(self):
        print("-----D-----Test")
        #print(self.a1, self.a2, self.b1, self.c1, self.d1)
        print(self.a2,self.d1)
    
    def testD(self):
        print("-----D-----TestD----")
        #print(self.a1, self.a2, self.b1, self.c1, self.d1)
        print(self.a2, self.d1)


if __name__ == "__main__":
    a = A()
    b = B()
    c = C()
    d = D()

    print("B:")
    b.test()
    b.testA()
    
    print("C:")
    c.test()
    c.testA()

    print("D:")
    d.test()
    d.testA()
    d.testD()

    print("d=a")
    d = a
    d.test()
    d.testA()
  #  d.testD()

