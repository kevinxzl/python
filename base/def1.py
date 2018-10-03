#encoding=utf-8
# 可写函数说明
def printinfo( arg1, arg2, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (arg2)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50, 'a', 'bc', 'efg' )