from functools import reduce


def add(x1, x2):
    return x1 + x2


arr = [1, 2, 3]
b = reduce(add, arr)
print(b)
