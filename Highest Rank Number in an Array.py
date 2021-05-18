# Given an array of integers, find the one that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.


from collections import defaultdict
def find_it(seq):
    # if len(seq) == 0:
    #     return None
    # col = collections.Counter(seq)
    # for i in col:
    #     if col[i] % 2 == 1:
    #         return i
    d = defaultdict(int)
    for k in seq:
        d[k] += 1
    return sorted(seq,key=lambda x: (seq.count(x),x))[-1]







print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
print(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))

# test.assert_equals(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), -1);
# test.assert_equals(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]), 5);
# test.assert_equals(find_it([10]), 10);
# test.assert_equals(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]), 10);
# test.assert_equals(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]), 1);