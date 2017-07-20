'''
非递归方式：
'''
class Solution:
    # @param n: An integer.
    # return : A list of integer storing 1 to the largest number with n digits.
    def numbersByRecursion(self, n):
        tmax = 1
        for i in range(n):
            tmax *= 10
        res = []
        for i in range(1,tmax):
            res.append(i)
        return res
