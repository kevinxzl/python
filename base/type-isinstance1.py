print("Test Case 1")
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

print("Test Case 2")
a = 111
print("isinstance(a, int)---", isinstance(a, int))

print("Test Case 3")

class A:
    pass

class B(A):
    pass

print("isinstance(A(), A)---", isinstance(A(), A))
print("type(A()) == A---", type(A()) == A)
print("isinstance(B(), A)---", isinstance(B(), A))
print("isinstance(A(), B)---", isinstance(A(), B))
print("type(B()) == A---", type(B()) == A)