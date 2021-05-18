# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
#
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

from collections import OrderedDict


def unique_in_order(iterable):
    # new = []
    # for i in range(0, len(iterable)-1):
    #     if iterable[i-1] != iterable[i]:
    #         new.append(iterable[i])
    # return new
    new = []
    for i in iterable:
        if len(new) < 1 or not i == new[len(new)-1]:
            new.append(i)
    return new



print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order(['a', 'a']))
print(unique_in_order(['a']))
