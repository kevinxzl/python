def fib1(n):
    if n <= 0:
        return 0

    i, a, b = 1, 0, 1
    while i < n:
        a, b = b, a + b
        i += 1
    return b


def fib2(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

def fib3(n):
    if n <= 0:
        return 0
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    
    return b


def fib4(n):
    if n <= 0:
        return 0
    
    if n == 1:
        return 1

    i, a, b = 1, 0, 1
    mList = []
    while i < n:
        a, b = b, a + b
        i += 1
        mList.append(b)
    
    return mList

def swap(a, b):
    a, b = b, a
    return a, b


if __name__ == "__main__":
    print("fib1(9)=", fib1(9))
    print("fib2(9)=", fib2(9))
    print("fib3(9)=", fib3(9))
    print("fib4(9)=", fib4(9))
    a, b = swap(10, 20)
    print(a, b)

