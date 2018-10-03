#encoding=utf-8
 
import copy
a = [1, 2, 3, 4, ['a', 'b']] #原始对象
print("原始对象")
print(a)
print("b=a") 
b = a                       #赋值，传对象的引用
print("c = copy.copy(a)")
c = copy.copy(a)            #对象拷贝，浅拷贝
print("d = copy.deepcopy(a)")
d = copy.deepcopy(a)        #对象拷贝，深拷贝
print("a.append(5)") 
print("a[4].append('c')")
a.append(5)                 #修改对象a
a[4].append('c')            #修改对象a中的['a', 'b']数组对象
 
print( 'a = ', a )
print( 'b = ', b )
print( 'c = ', c )
print( 'd = ', d )