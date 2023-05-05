from typing import List


def partition(nums, low, high) -> int:
    piv = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] <= piv:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[high] = nums[high], nums[i]
    return i


def quick_sort(nums: List, low, high):
    if low < high:
        p = partition(nums, low, high)
        quick_sort(nums, low, p - 1)
        quick_sort(nums, p + 1, high)


def sort(nums):
    quick_sort(nums, 0, len(nums) - 1)
    return nums


print(sort([5, 8, 1, 4, 7, 9, 6, 3, 2]))
print(sort([]))
print(sort([0, 1, 2, 6, -1]))
