# Complete the method which returns the number which is most frequent in the given input array. If there is a tie for
# most frequent number, return the largest number among them.
#
# Note: no empty arrays will be given.
#
# Examples
#
# [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
# [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

#solutie 1 import statistics
# def highest_rank(arr):
#     mode = [statistics.mode(arr)]
#     if len(mode) > 1:
#         return max(mode)
#     return mode[0]

# solutie 1
# def highest_rank(arr):
    # counter = 0
    # num = arr[0]
    #
    # for i in arr:
    #     curr_frequency = arr.count(i)
    #     if (curr_frequency > counter):
    #         counter = curr_frequency
    #         num = i
    # return num

# solutia 3

    # dict = {}
    # count, itm = 0, ''
    # for item in reversed(arr):
    #     dict[item] = dict.get(item, 0) + 1
    #     if dict[item] >= count:
    #         count, itm = dict[item], item
    # return (item)

# sol 4
#     counte = arr.count
#     return max(set(arr), key=counte)
#
# sol 5
from collections import defaultdict


def highest_rank(arr):
    d = defaultdict(int)
    for k in arr:
      d[k] += 1
    return max(list(d.keys())) if(len(set(d.values())) == 1) else max(d, key=d.get)



print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]))