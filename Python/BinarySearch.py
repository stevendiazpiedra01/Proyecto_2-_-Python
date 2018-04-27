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
l = input()
a= l.split(",")
c = []
d=input("ingrese numero");
for i in range(0, len(a),1):
    c.append(a[i])

print (binarysearch(c,d))
print (binarysearch([1,5,6,9,10,11,15,78],78))
