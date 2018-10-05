class People(object):
    __addr = 'BJ'
    __count = 0
    def __init__(self, name):
        self.name = name
        self.age  = 18
        People.__count += 1

    def getInfo(self):
        print("name=%s, age=%d" %(self.name, self.age), self.__count)
    
    @classmethod
    def setAddr(cls, addr):
        cls.__addr = addr
    
    @classmethod
    def getAddr(cls):
        return cls.__addr
    
    @classmethod
    def getCount(cls):
        return cls.__count

if __name__ == "__main__":
    p1 = People("XiaoMing")
    print(p1.getCount())
    p1.setAddr("BeiJing")

    p2 = People("LeiGong")
    print(p1.getCount())
    p2.setAddr("YunNan")

    People.setAddr("USA")
    #People.getInfo()
    print(p1.getAddr(), p1.name, p1.age)
    print(p2.getAddr(), p2.name, p2.age)
    p1.getInfo()
    p2.getInfo()
    