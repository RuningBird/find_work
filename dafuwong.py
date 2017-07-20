# 大富翁游戏，玩家根据骰子的点数决定走的步数，即骰子点数为1时可以走一步，点数为2时可以走两步，点数为n时可以走n步。
# 求玩家走到第n步（n<=骰子最大点数且是方法的唯一入参）时，总共有多少种投骰子的方法。
# 输入描述:6->32
# 输入包括一个整数n,(1 ≤ n ≤ 6)

def result(n):
    if n == 0:
        return 0
    dp = [1 for i in range(n + 1)] # 1-6
    for i in range(2, n + 1):
        dp[i] = 0
        for j in range(0, i):
            dp[i] += dp[j]
    return dp[n]

n = int(input())
print(result(n))
