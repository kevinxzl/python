#encoding=utf-8

def freq(mList):
    mDict = {}
    resList = []
    for i in mList:
        if not mDict.get(i):
            mDict[i] = 1
        else:
            mDict[i] += 1
    
    printDict(mDict)
    max = 0
    for k, v in mDict.items():
        if max == v:
            resList.append(k)

        if v > max:
            resList.clear()
            resList.append(k)
            max = v
            
    return resList

def printDict(mDict):
    for k, v in mDict.items():
        print(k,"---",v)
        
if __name__ == '__main__':
    la = [-9,2,4,5,7,8,2,9,6,10,8,-9,0,4,0,2,5,7, 4, 5,6,9,2,6,5,6, 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 6]
    mList = freq(la)
    print(mList)
    
