a = [4, 5, 6, 7, 1, 2, 3]


def find_min(nums):
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2

    if nums[0] == nums[left] and nums[0] == nums[mid]:
        return min(nums)
    # else:
        # while(nums[left] <= nums[right])

