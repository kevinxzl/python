mList = [ ]
for i in range(5):
    mList.append(i)

print(mList)

for i in range(10, 15):
    mList.append(i)

print(mList)

print("insert abcd in index = 3")
mList.insert(3, 'abcd')
print(mList)

print("find value = 10 and then insert 100 after")
index = mList.index(10)
index += 1
mList.insert(index, 10 * 10)
print(mList)

print("del mList[2]  index =2 value")
del mList[2]
print(mList)

print("remove value = 14 ")
mList.remove(14)
print(mList)

print("for in mList")
for item in mList:
    print(item)