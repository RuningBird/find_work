# class Solution:
#     """
#     @param nums: A list of integers
#     @return: The majority number
#     """
#     def majorityNumber(self, nums):
#         resc = -1 # 统计出现次数
#         res = -1
#         for each in nums:
#             val = nums.count(each)
#             if val > resc:
#                 resc = val
#                 res = each
#         return res

nums = [1, 1, 1, 1, 2, 2, 2]


# so = Solution()
# res = so.majorityNumber(nums)
# print(res)


def majorityNumber(nums):
    for each in nums:
        val = nums.count(each)
        if val > len(nums) // 2:
            return each


valres = majorityNumber(nums)
print(valres)
