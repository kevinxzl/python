def rm_rep_ele1(mList):
    return set(mList)

def rm_rep_ele2(mList):
    l2 = {}.fromkeys(mList).keys()
    print(l2)

if __name__ == '__main__':
    mList =  [1,2,2,2,2,3,3,3,4,4,4,4]

    print("Test Case 1:")
    mSet = rm_rep_ele1(mList)
    print(mSet)

    print("Test Case 2:")
    rm_rep_ele2(mList)