class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """

    # 循环解法
    def maxSubArray(self, nums):
        if nums:
            max_val = -0xffffffff
            current = 0
            for each in nums:
                if current <= 0:
                    current = each
                else:
                    current += each

                if current > max_val:
                    max_val = current
            return max_val
        else:
            return None

    # 动态规划解法
    def dynamic_programing(self, nums):
        nums2 = [-0xffffffff]
        nums2.extend(nums[::])
        f = [0 for i in range(len(nums2))] # 0 为前0个数，加起来的最大值，因为没有数，取0
        for i in range(1, len(nums2)):
            if f[i - 1] + nums2[i] > f[i]:
                f[i] = f[i - 1] + nums2[i]
            else:
                f[i] = f[i - 1]
        res = f[len(nums2) - 1]
        return res


nums = [-2, 2, -3, 4, -1, 2, 1, -5, 3]
so = Solution()
res = so.maxSubArray(nums)
print(res)
res2 = so.dynamic_programing(nums)
print(res2)
