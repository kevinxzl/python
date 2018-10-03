def refq1(mList):
    mMap = { }
    for i in mList:
        mMap[i] = mList.count(i)
    
    return mMap


if __name__ == '__main__':
    mList =  [1,2,3,4,3,4,4,4,4]
    mMap = refq1(mList)
    print(mMap)
