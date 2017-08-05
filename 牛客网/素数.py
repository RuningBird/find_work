'''
输入M、N，1 < M < N < 1000000，求区间[M,N]内的所有素数的个数。素数定义：除了1以外，只能被1和自己整除的自然数称为素数
输入描述:
两个整数M，N


输出描述:
区间内素数的个数

输入例子1:
2 10

输出例子1:
4
'''


def change(snum):
    return int(snum)


# 是否是素数
def is_prime_number(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return []
    return num


tnum = [i for i in range(2, 20)]
res = list(map(is_prime_number, tnum))


print('原始：', tnum)
print('结果：', list(res))













# ins  = input()
# sarr = ins.split(' ')
# iarr = map(change, sarr)
