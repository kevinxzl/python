def fib1(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


def fib2(n):
    if n == 0:
        return 0

    a, b, sum = 0, 1, 0
    n += 1
    for i in range(2, n):
        sum = a + b
        a, b = b, a + b
    return b

def fib3(n):
    if n == 0:
        return 0
    
    a, b ,sum, i = 0, 1, 0, 2
    while i <= n:
        sum = a + b
        a, b = b, a+b
        i += 1
    return b

print(fib1(19))
print(fib2(19))
print(fib3(19))