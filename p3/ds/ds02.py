def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


print("Test Case 1")
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

print("Test Case 2")
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)

print("Test Case 3")
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


print("Test Case 4")
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print(sum(items))
