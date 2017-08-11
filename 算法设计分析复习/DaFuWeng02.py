def result(n):
    if n == 0:
        return 1
    else:
        return 2 ** (n - 1)
n = int(input())
print(result(n))
