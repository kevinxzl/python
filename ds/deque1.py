
class Deque(object):
    def __init__(self):
        self.__list = []
    
    def add_front(self, item):
        self.__list.insert(0, item)

    def add_rear(self, item):
        self.__list.append(item)

    def pop_front(self):
        return self.__list.pop(0)

    def pop_rear(self):
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)
    

if __name__ == "__main__":
    dq = Deque()
    dq.add_front(1)
    dq.add_front(3)
    dq.add_rear(2)
    dq.add_rear(4)
    
    print("Size:", dq.size())
    print("pop from front")
    print(dq.pop_front(), end="  ")
    print(dq.pop_front(), end="  ")
    print()
    print("pop from end")
    print(dq.pop_rear(), end=" ")
    print(dq.pop_rear(), end=" ")
    print()

    