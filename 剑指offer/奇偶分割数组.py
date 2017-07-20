# 自写版
def partitionArray(nums):
    ou = []
    for i in nums:
        if i % 2 == 0:
            ou.append(i)
            nums.remove(i)
    nums.extend(ou)
    return nums


# 强制版
def partitionArray2(nums):
    if not nums:
        return None
    start = 0
    end = len(nums) - 1

    while start < end:
        while start < end and nums[start] % 2:
            start += 1
        while start < end and not nums[end] % 2:
            end -= 1
        if start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp



num = [1, 2, 3, 4]
num2 = [402, 455, 25, 15, 42, 538, 369, 741, 651, 473, 310, 112, 525, 682, 622, 119, 287, 242, 701, 439]

partitionArray2(num)
print(num)
