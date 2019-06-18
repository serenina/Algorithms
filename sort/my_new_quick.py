import random


def __quicksort(x, lo, hi):
    if lo < hi:
        p = partition(x, lo, hi)
        __quicksort(x, lo, p - 1)
        __quicksort(x, p + 1, hi)
    return x


# @profile
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
    return __quicksort(x, 0, len(x) - 1)
