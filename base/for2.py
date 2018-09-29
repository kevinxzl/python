print("Test Case 1")
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")


print("Test Case 2")
for letter in 'Runoob':     # 第一个实例
   if letter == 'b':
      break
   print ('当前字母为 :', letter)
  
var = 10                    # 第二个实例
while var > 0:              
   print ('当期变量值为 :', var)
   var -= 1
   if var == 5:
      break
 
print ("Good bye!")

print("Test Case 3")
for letter in 'Runoob':     # 第一个实例
   if letter == 'o':        # 字母为 o 时跳过输出
      continue
   print ('当前字母 :', letter)
 
var = 10                    # 第二个实例
while var > 0:              
   var -= 1
   if var % 2 == 0:             # 变量为 5 时跳过输出
      continue
   print ('当前变量值 :', var)
print ("Good bye!")


print("Test Case 4")
for i in range(2, 10):
    for j in range(2, i):
        if i % j == 0:
            print(i, '等于', j, '*', i//j)
            break
    else:
        # 循环中没有找到元素
        print(i, ' 是质数')

print("Test Case 5")
for letter in 'Runoob': 
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")