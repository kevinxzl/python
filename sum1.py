#encoding=utf-8
def swap(a, b):
    a, b = b, a
    print("a addr in swap= ", id(a))
    return a, b

def sum1(a, *b):
    res = 0
    res += a
    for x in b:
        res += x
    
    return res

def sum2(a, *b, **c):
    res = 0
    res += a
    for x in b:
        res += x
    
    return res


def sum3(num):
    res = 0
    if num > 1:
        return num + sum3(num-1)
    else:
        res = 1
    
    return res


if __name__ == "__main__":
    a, b = 10, 20
    print("a addr=", id(a))
    print("a=%d, b=%d"% (a, b))
    a, b = swap(a, b)
    print("swap(a,b)")
    print("a=%d, b=%d"% (a, b))

    print(sum1(1,22,33,5,23,56))
    print(sum2(1,2,3,4,5,m=23,n=56))
    print(sum3(4))