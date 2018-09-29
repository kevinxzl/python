from timeit import Timer

'''
l1 = [1, 2]
l2 = [23, 5]
l3 = l1 + l2 
l4 = [i for in range(10000)]
l5 = list(range(10000))
l6 = []
'''

def test1():
    li = []
    for i in range(10000):
        li.append(i)

def test2():
    li = []
    for i in range(10000):
        li += [i]  # [] + [1]

#list generator 
def test3():
    li = [i for i in range(10000)]

def test4():
    li = list(range(10000))

def test5():
    li = []
    for i in range(10000):
        li.extend([i])

def test6():
    li = []
    for i in range(10000):
        li.insert(0, i)


t1 = Timer("test1()", "from __main__ import test1")
print("append", t1.timeit(1000)) #run 1000 times

t6 = Timer("test6()", "from __main__ import test6")
print("insert to head", t6.timeit(1000))


t2 = Timer("test2()", "from __main__ import test2")
print("+", t2.timeit(1000))

t3 = Timer("test3()", "from __main__ import test3")
print("list generator", t3.timeit(1000))

t4 = Timer("test4()", "from __main__ import test4")
print("use list() transfer", t4.timeit(1000))

t5 = Timer("test5()", "from __main__ import test5")
print("extend", t5.timeit(1000))

