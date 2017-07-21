
#Since I find the mergeSort too complicated for me, I decided to split it in different functions

import time

nums = [54,26,93,17,77,31,44,55,80]


#This function split an array of n elements into n-sub-arrays
def split(x):
    newx = []
    for i in range(0, len(x)):
        newx.append([x[i]])
    return newx

nums = split(nums)
print nums

#this function merge and sort two arrays, not necessarily of the same size but that are already sorted

def merge2lists(x, y):
    newlist = []
    t = 0 # counter index for x
    k = 0 # counter index for y
    while len(newlist) != len(x) + len(y): # the function is stopping when all the elements of x and y are merged in newlist
        if t == len(x): # this check if all the elements of x have been tested
            newlist += y[k:]
        elif k == len(y):  # this check if all the elements of y have been tested
            newlist += x[t:]
        elif x[t] < y[k] and t < (len(x)):  # this check which element of x and y is bigger and then append it to newlist
            newlist.append(x[t])
            t += 1
        else:
            newlist.append(y[k])
            k +=1
    return newlist

# this function merge several lists
def mergelists(x):
    newlist = x
    newlist2 = []
    # the following if check if the array is even or odd
    if len(newlist)%2 != 0:
        # in this case I have to remove the last element to have an even array and then is merging-sorting again at the end
        scrap = newlist.pop()
        while len(scrap) > 0:
            while len(newlist) != 1:
                dumping = []
                for i in range(0, len(newlist), 2):
                    dumping += [merge2lists(newlist[i], newlist[i+1])]
                newlist = dumping
            for i in range(0, len(newlist)): # I needed to do this loop because the merge2list function return a list of a list ([[]]) when reiterate.
                                             # If so the last merge2list doesn't work and the program doesn't merge sort the scrap
                newlist2 += newlist[i]
            newlist2 = merge2lists(newlist2, scrap)
            scrap.pop()
    else:
        while len(newlist) != 1:
            dumping = []
            for i in range(0, len(newlist), 2):
                dumping += [merge2lists(newlist[i], newlist[i+1])]
            newlist = dumping
        for i in range(0, len(newlist)):
            newlist2 += newlist[i]
    return newlist2

print (mergelists(nums))