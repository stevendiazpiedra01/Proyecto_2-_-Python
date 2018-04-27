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


l = input()
al = l.split(",")
c=[]
d=int(input("ingrese numero"));
for i in range (len(al)):
   c.append(int(al[i]))
   
result = binarysearch_recursive(c, d,0 , len(c) - 1)



if result != -1:
    print ("El numero esta en el indice %d" % result)
else:
    print ("El numero no esta presente en el arreglo")
