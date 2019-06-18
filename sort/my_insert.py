import time


def insert_sort(x):
    for i in range(1, len(x)):
        currentvalue = x[i]
        index = i
        while index > 0 and x[index - 1] > currentvalue:
            x[index] = x[index - 1]
            index = index - 1
            # print (currentvalue, index, i)
            # print (x)
        x[index] = currentvalue
        # print (currentvalue, index, i)
        # print x
    return x
