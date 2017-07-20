# 给你六种面额 1、5、10、20、50、100 元的纸币，假设每种币值的数量都足够多，编写程序求组成N元（N为0~10000的非负整数）的不同组合的个数。
# 输入: 整数n(1 ≤ n ≤ 10000)
# 输出: 输出一个整数,表示不同的组合方案数


def result(total):
    coins = [1, 5, 10, 20, 50, 100]
    len1 = coins.__len__()
    dp = [[0 for i in range(total + 1)] for i in range(len1)]
    for i in range(len1):
        dp[0][i] = 0
        dp[i][0] = 1
    for i in range(1, len1 + 1):
        for j in range(1, total + 1):
            m = j / coins[i - 1]
            for k in range(0, int(m) + 1):
                dp[i][j] += dp[i - 1][j - k * coins[i - 1]]
    return dp[len1 - 1][total]


# n = int(input())
print(result(10))
