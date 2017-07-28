from sort.my_bubble import bubble_sort

import random

def series():
    for i in range(1, 1001, 50):
        x = random.sample(xrange(1000), i)
        print x
        return x

series()