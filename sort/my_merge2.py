def split(x):
    newx = []
    for i in range(0, len(x)):
        newx.append([x[i]])
    return newx


def merge2lists(x, y):
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
            k += 1
    return newlist


def mergelists(x):
    newlist = split(x)
    newlist2 = []

    if len(newlist) % 2 != 0:
        if len(x) == 1:
            newlist2 = x
        else:
            scrap = newlist.pop()
            while len(scrap) > 0:
                while len(newlist) != 1:
                    dumping = []
                    for i in range(0, len(newlist), 2):
                        dumping += [merge2lists(newlist[i], newlist[i + 1])]
                    newlist = dumping
                for i in range(0, len(newlist)):
                    newlist2 += newlist[i]
                newlist2 = merge2lists(newlist2, scrap)
                scrap.pop()
    else:
        while len(newlist) != 1:
            dumping = []
            for i in range(0, len(newlist), 2):
                dumping += [merge2lists(newlist[i], newlist[i + 1])]
            newlist = dumping
        for i in range(0, len(newlist)):
            newlist2 += newlist[i]
    return newlist2
