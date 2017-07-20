arr = [i for i in range(20 + 1)]
arr2 = [1, 2, 3]


def isOuShu(x):
    return not x % 2


def pew(x):
    return x ** 2


# res = map(isOuShu,arr)
res = map(pew, arr)

print(res, arr, type(res))
for i in res:
    print(i, end=' ')
