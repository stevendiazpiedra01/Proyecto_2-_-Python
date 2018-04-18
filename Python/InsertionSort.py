def InsertionSort (a):
    for i in range (1,len(a)):
        x=a[i]
        index=i

        while index > 0 and  a[index-1] > x:
            a[index]=a[index-1]
            index = index -1
    a[index] = x

a = [54,265,68,98,75]
InsertionSort(a)
print(a)