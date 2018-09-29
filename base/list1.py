print("访问列表中的值")
list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c', 'aabcd' ];
print(list1)
print(list2)
print ("list1[0]: ", list1[0])
print("list2[:]", list2[:])
print ("list2[1:5]: ", list2[1:5])

print("更新列表")
list = ['Google', 'Runoob', 1997, 2000]
 
print ("第三个元素为 : ", list[2])
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2])

print("删除列表元素")

list = ['Google', 'Runoob', 1997, 2000]
 
print ("原始列表 : ", list)
del list[2]
print ("删除第三个元素 : ", list)