def fib1(n):
    i, a, b = 0, 0, 1
    while i < n:
        a, b = b, a + b
        i += 1
    return b

def fib2(n):
    pass

    
def fib3(n):
    i, a, b = 0, 0, 1
    mList = []
    while i < n:
        a, b = b, a + b
        i += 1
        mList.append(b)
    
    return mList


if __name__ == "__main__":
    print("fib1(5)=",fib1(5))
    print("fib3(5)=", fib3(5))

