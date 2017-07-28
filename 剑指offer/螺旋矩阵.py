class Solution:
    # @param {int[][]} matrix a matrix of m x n elements
    # @return {int[]} an integer array
    ans = []
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [12, 13, 14, 15]
    ]

    def spiralOrder(self, matrix):
        # self.matrix = matrix
        while self.matrix:
            ###########################################
            # 用于判断a= [[],[],[],...]，此时列表已经为空
            b = True  #
            for i in self.matrix:
                if i:
                    b = False
            if b:
                break
            ###########################################

            self.so()

        return self.ans

    def so(self):
        # 上
        if self.matrix:
            row = self.matrix[0][::]
            self.ans.extend(row)

            self.matrix.remove(row)

        # 右
        if self.matrix:
            right = []
            cl = len(self.matrix[0]) - 1  # 列长度
            for i in range(len(self.matrix)):
                val = self.matrix[i][cl]
                right.append(val)  # 取出右边的元素
                self.matrix[i].remove(val)

            self.ans.extend(right)

        # 下
        if self.matrix:
            rl = len(self.matrix) - 1
            bottom = self.matrix[rl]
            rv_b = bottom[::-1]

            self.ans.extend(rv_b)
            self.matrix.remove(bottom)

        # 左
        if self.matrix:
            left = []
            for i in range(len(self.matrix)):
                val = self.matrix[i][0]
                left.insert(0, val)
                self.matrix[i].remove(val)
            self.ans.extend(left)

    def show_ans(self):
        print(self.ans)


arr = []
so = Solution()
so.spiralOrder(arr)

so.show_ans()
