#encoding=utf-8
import copy

print("copy")
dict1 =  {
    'user':'runoob',
    'num':[10,20,30]
}
 
dict2 = dict1          # 浅拷贝: 引用对象
dict3 = dict1.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
dict4 = copy.deepcopy(dict1) # 深度拷贝需要引入 copy 模块：

print("dict1")
print(dict1)
print("dict2 = dict1 ")
print("dict2")
print(dict2)
print("dict3 = dict1.copy() ")
print(dict3)
print("dict4 = copy.deepcopy(dict1)")
print(dict4)
# 修改 data 数据
print("修改 data 数据")
dict1['user']='root'
dict1['num'].remove(10)
 
# 输出结果
print("dict1----")
print(dict1)
print("dict2----")
print(dict2)
print("dict3----")
print(dict3)
print("dict4------------------")
print(dict4)

