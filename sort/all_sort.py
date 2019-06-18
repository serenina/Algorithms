
#bubble sort

def bubble_sort(x):
    for i in range(len(x) - 1, 0, -1):
        for j in range(i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x



#insert sort

def insert_sort(x):
    for i in range(1, len(x)):
        currentvalue = x[i]
        index = i
        while index > 0 and x [index - 1] > currentvalue:
            x[index] = x[index - 1]
            index = index - 1
        x[index] = currentvalue
    return x


#merge sort

def merge_sort(x):

    if len(x) < 2:return x

    result,mid = [],int(len(x)/2)

    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])

    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:result.append(z.pop(0))
            else:result.append(y.pop(0))

    result.extend(y+z)
    return result


#quick sort


def __quicksort(x, lo, hi):
    if lo < hi:
        p = partition(x, lo, hi)
        __quicksort(x, lo, p - 1)
        __quicksort(x, p + 1, hi)
    return x


def partition(x, lo, hi):
    pivot = x[hi]
    i = lo - 1
    for j in range(lo, hi):
        if x[j] < pivot:
            i += 1
            x[i], x[j] = x[j], x[i]
    if x[hi] < x[i + 1]:
        x[i + 1], x[hi] = x[i + 1], x[hi]
    x[hi], x[i + 1] = x[i + 1], x[hi]
    return i + 1

def quicksort(x):
    return __quicksort(x, 0, len(x)-1)
