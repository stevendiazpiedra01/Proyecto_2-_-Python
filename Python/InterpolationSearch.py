def interpolationsearch ( a, x):
    lowerbound = 0
    upperbound = len(a)-1
    index = -1

    while lowerbound < upperbound:
        middlepoint = lowerbound + ((upperbound-lowerbound)//(a[upperbound] - a[lowerbound])) * (x - a[lowerbound])
        if x == a[middlepoint]:
            index = middlepoint
            break
        else:
            if x < a [middlepoint]:
                upperbound = middlepoint - 1
            else:
                lowerbound = middlepoint + 1

    if lowerbound == upperbound and a[lowerbound] == x:
        index = lowerbound

    return index


index = interpolationsearch([10, 12, 13, 16, 18, 19, 20, 21,22, 23, 24, 33, 35, 42, 47], 84)

if index != -1:
    print ("El numero esta en el indice %d" % index)
else:
    print ("El numero no esta presente en el arreglo")
