import sys


def findminJump(arr):
    if arr[0] == 0:
        return sys.maxsize
    n = len(arr)
    lookup = [sys.maxsize] * n
    lookup[0] = 0
    for i in range(n):
        j = 1
        while (i + j < n) and j <= min(n - 1, arr[i]):
            lookup[i + j] = min(lookup[i + j], lookup[i] + 1) \
                if (lookup[i + j] != sys.maxsize) else (lookup[i] + 1)
            j = j + 1
    return lookup[n - 1]

mov = range(1, 200)
print("the min moves: ", findminJump(mov))
