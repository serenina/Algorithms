import time
# def quick_sort(x):
#     wall = 0
#     pivot = len(x) - 1
#     current_position = 0
#     newlist = x
#     for i in range(0,len(x)):
#         if x[i] < x[pivot]:

nums = [6,10,8,1,3]

def quick_sort(x):
    l_list = []
    r_list = []
    if len(x)<= 1:
        return x
    for i in range(1, len(x)):
        if x[i] > x[0]:
            r_list.append(x[i])
        else:
            l_list.append(x[i])
    print l_list, r_list
    l_list.append(x[0])
    new_list = quick_sort(l_list) + quick_sort(r_list)
    print new_list
    return new_list



print nums, quick_sort(nums)