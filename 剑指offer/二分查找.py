a = [0, 1, 2, 3, 4, 5]


def binary_search(nums, key):
    low = 0
    high = len(nums) - 1
    mid = (low + high) // 2
    while low <= high:
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            low = mid + 1
        else:
            high = mid - 1


index = binary_search(a, 2)
print(a[index], ',index-', index)
