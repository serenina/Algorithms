# import random
import pytest
import time

#profiler
def bubble_sort(x):
    for i in range(len(x) - 1, 0, -1):
        for j in range(i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
        return x

# print ("How many elements do you want in your list?")
# n = input()

# alist = random.sample(xrange(1000), n)

nums = [54,26,93,17,77,31,44,55,20]

print "Your list is:", nums
start = time.time()
bubble_sort(nums)
end = time.time()
print "Your sorted list is:", nums
print ("Found min number {} and max number {} in {} seconds".format(nums[0], nums[len(nums) - 1], (end - start)))

def test_bubble():
    assert bubblesort(nums) == sorted(nums)
