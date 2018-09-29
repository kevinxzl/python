basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # 这里演示的是去重功能

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)

c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)