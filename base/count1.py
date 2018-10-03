#encoding=utf-8

str="www.runoob.com"
print(str)
sub='o'
print ("str.count('o') : ", str.count(sub))

sub='run'
print ("str.count('run) : ", str.count(sub))
print ("str.count('run', 0, 10) : ", str.count(sub,0,10))


la = [1, 2, 4, 5, 6, 8, 2, 4, 6, 8]
print(la)
for i in la:
    if la.count(i) >= 2:
        print("第一个重复的元素是:%d" %i)
        break