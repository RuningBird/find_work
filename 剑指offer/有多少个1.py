# def count_ones(num):
#     n = abs(num)
#     n1 = bin(n)
#     n2 = n1[2:]
#     n3 = n2.replace('0', '')
#     return len(n3)

def countOnes(num):
    num = num & (0xffffffff)
    count = 0
    while (num):
        count += 1
        num = num & (num - 1)
    return count


num = -1
r = countOnes(num)
print(bin(num), r)
