import time

nums = [54,26,93,17,77,31,44,55,20]
def insert_sort(x):
    for i in range(1, len(x)):
        currentvalue = x[i]
        index = i
        while index > 0 and x [index - 1] > currentvalue:
            x[index] = x[index - 1]
            index = index - 1
            # print (currentvalue, index, i)
            # print (x)
        x[index] = currentvalue
        # print (currentvalue, index, i)
        # print x
    return x

a = insert_sort(nums)

print a