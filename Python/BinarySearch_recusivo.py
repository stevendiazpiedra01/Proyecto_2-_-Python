def binarysearch_recursive (a, x , lb , ub):
    middlepoint = (lb+ub)//2
    if lb == ub :
        if x == a[middlepoint]:
            return middlepoint
        else:
            return -1
    else:
        if x == a [middlepoint]:
            return middlepoint
        else:
            if x < a[middlepoint]:
                return binarysearch_recursive(a,x,lb,middlepoint)
            else:
                return binarysearch_recursive(a,x,middlepoint +1,ub)

a = [2,3,4,10,40]
x = 8
result = binarysearch_recursive(a, x,0 , len(a) - 1)

if result != -1:
    print ("El numero esta en el indice %d" % result)
else:
    print ("El numero no esta presente en el arreglo")