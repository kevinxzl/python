#encoding=utf-8

def freq(mList):
    mDict = {}
    for i in mList:
        if not mDict.get(i):
            mDict[i] = 1
        else:
            mDict[i] += 1
    
    return mDict

def printDict(mDict):
    for k, v in mDict.items():
        print(k,"---",v)
        





if __name__ == '__main__':
    la = [-9,2,4,5,7,8,2,9,6,10,8,-9,0,4,0,2,5,7, 4, 5,6,9,2,6,5,6]
    mDict = freq(la)
    printDict(mDict)
