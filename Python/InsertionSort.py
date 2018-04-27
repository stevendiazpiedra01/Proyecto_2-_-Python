def InsertionSort (a):
    for i in range (1,len(a)):
        x=a[i]
        index=i

        while index > 0 and  a[index-1] > x:
            a[index]=a[index-1]
            index = index -1
    a[index] = x


l = input()
al = l.split(",")
c=[]

for i in range (len(al)):
   c.append(int(al[i]))
InsertionSort(c)
print(c)
