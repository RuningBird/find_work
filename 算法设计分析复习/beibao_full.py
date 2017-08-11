N = 4  # 物品个数
M = 10  # 背包容量
x = [0 for i in range(5)]  # 标记变量，物品是否选择，全部不选中
w = [0, 5, 4, 6, 3]  # 物品重量, 0 位置不用
v = [0, 10, 40, 30, 50]  # 物品价值，同上
f = [0 for i in range(M + 1)]  # 价值矩阵

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if w[i] < j:
            # f[i + 1][j] = max(f[i][j - k * weight[i + 1]] + k * value[i + 1])
            put = f[j - w[i]] + v[i]
            un_put = f[j]
            f[j] = max(put,un_put)
print(f[M])
