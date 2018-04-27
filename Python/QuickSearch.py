def quicksort(a):
    high = []
    low = []
    pivot_list = []

    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        for i in a:
            if i < pivot:
                low.append(i)
            elif i > pivot:
                high.append(i)
            else:
                pivot_list.append(i)
        high = quicksort(high)
        low = quicksort(low)

    return low + pivot_list + high

l = input()
a= l.split(",")
c = []
for i in range(0, len(a),1):
    c.append(a[i])
    
print (quicksort(c))
