langs = ["C", "C++", "Perl", "Go", "Java", "Python"]
print("Test Case 1")
for x in langs:
    print(x)

print("Test Case 2")
for i in range(len(langs)):
    print(i, '---', langs[i])


print("Test Case 3")
for i in range(5):
    print(i)

print("Test Case 4")
for i in range(5,9):
    print(i)

print("Test Case 5")
for i in range(1, 10, 3):
    print(i)



print("Test Case 6")
list1 = list(range(5))
print(list1)