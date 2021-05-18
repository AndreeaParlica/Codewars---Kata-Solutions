# You get an array of numbers, return the sum of all of the positives ones.
#
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
#
# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    items = [x for x in arr]
    count = 0
    positive = []
    for i in items:
        if i > 0:
            positive.append(i)
    for j in positive:
        count += j
    return count



print(positive_sum([1,2,3,4,5]))
      # ,15)
print(positive_sum([1,-2,3,4,5]))
# ,13)
print(positive_sum([-1,2,3,4,-5]))
# ,9)