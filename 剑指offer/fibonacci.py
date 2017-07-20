def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def fic(n):
    n1 = 0
    n2 = 1
    n3 = 0
    for i in range(3,n+1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return n3

print(fic(2))


# for i in range(10):
#     print(fibonacci(40))
