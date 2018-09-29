p = (4, 5)
x, y = p
print("Test Case 1")
print(x)
print(y)

print("Test Case 2")
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
name, shares, price, (year, mon, day) = data
print(name)
print(shares)
print(price)
print(date)
print(year)
print(mon)
print(day)

print("Test Case 3")
s = "Hello"
a, b, c, d, e = s
print(a)
print(b)
print(c)
print(d)
print(e)

print("Test Case 4")
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)
