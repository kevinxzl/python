#encoding=utf-8

class A():
    _name = 'protected类型的变量'
    __info = '私有类型的变量'
    def _func(self):
        print("这是一个protected类型的方法", self._name)
    def __func2(self):
        print('这是一个私有类型的方法')
    def get(self):
        return(self.__info)

if __name__ == "__main__":
    a = A()
    print(a._name)
    a._func()
