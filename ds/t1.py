import time

t1 = time.time()

for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a+b+c == 1000 and a**2 + b**2 == c**2:
                print("a=%d, b=%d, c=%d" % (a, b, c))

t2 = time.time()

print("Time: %d" % (t2-t1))