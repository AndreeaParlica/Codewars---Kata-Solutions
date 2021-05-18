moves = []


# Minimum number of jumps to reach end
def functie(n, arr):
    if n == 1:
        return 0
    if arr[n] != -1:
        return arr[n]
    res = functie(n - 1, arr)
    if n % 2 == 0:
        res = min(res, functie(n // 2, arr))
    arr[n] = 1 + res
    return arr[n]


def functie_1(n):
    arr = [0 for i in range(n + 1)]
    for i in range(n + 1):
        arr[i] = -1
    return functie(n, arr)


n = 200
print(functie_1(n))

def min_jump(arr, n):
    jumps = [0 for i in range(n)]
    if (n == 0) or (arr[0] == 0):
        return float('inf')
    jumps[0] = 0
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if (i<=j + arr[j]) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n-1]
items = [x for x in range(1,200)]
print(min_jump(items, 200))