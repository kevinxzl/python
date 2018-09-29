import sys

print("Test Case 1")
l1 = [2, 4, 5, 8]
it = iter(l1)
print(it)
print(next(it)) #2
print(next(it)) #4
print(next(it)) #5
print(next(it)) #8
#print(next(it)) 

print("Test Case 2")
l2 = list(range(5))
it = iter(l2)
for x in it:
    print(x, end=" ")
print("\n")

print("Test Case 3")
l3 = [1, 2, 3, 4]
it = iter(l3)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()


print("Test Case 3")
