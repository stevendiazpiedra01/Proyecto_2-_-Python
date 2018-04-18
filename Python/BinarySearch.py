def binarysearch(a,x):
    lowerbound = 0
    upperbound = len(a)-1
    index = -1
    while lowerbound < upperbound:
        middlepoint = (lowerbound+upperbound)//2
        if x == a[middlepoint]:
            index = middlepoint
            break
        else :
            if x < a[middlepoint] :
                upperbound = middlepoint-1
            else :
                lowerbound = middlepoint + 1


    if lowerbound == upperbound and a[lowerbound] == x:
        index = lowerbound

    return index

print (binarysearch([1,2,3,5,8],8))
print (binarysearch([1,2,3,5,8],5))
