import time

numsa = [54,26,93,17]
numsb = [77,31,44,55,20]

nums = [54,26,93,17,77,31,44,55]

def split(x):
    newx = []
    for i in range(0, len(x)):
        newx.append([x[i]])
    return newx


nums = split(nums)
print nums

# def merge1(x):
# newx = []
# index = 0
# while index < len(x) and len(x) > 2:
#     if len(x) - index == 1:
#         newx.append(x[index])
#         index += 1
#     else:
#         if x[index] < x[index + 1]:
#             unit = x[index] + x[index + 1]
#             newx.append(unit)
#         else:
#             unit = x[index + 1] + x[index]
#             newx.append(unit)
#         index += 2
# return newx



numsa = [54,26,93,17]
numsb = [77,31,44,55, 80]

numsa = sorted(numsa)
numsb = sorted(numsb)
def merge3(x, y):
    newlist = []
    t = 0
    k = 0
    while len(newlist) != len(x) + len(y):
        if t == len(x):
            newlist += y[k:]
        elif k == len(y):
            newlist += x[t:]

        elif x[t] < y[k] and t < (len(x)):
            newlist.append(x[t])
            t += 1
        else:
            newlist.append(y[k])
            k +=1
    return newlist

def foo(x):
    newlist = x
    while len(newlist) != 1:
        scarico = []
        for i in range(0, len(newlist), 2):
            scarico += [merge3(newlist[i], newlist[i+1])]
        newlist = scarico
    return newlist





print (foo(nums))
