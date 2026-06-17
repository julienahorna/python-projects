def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
             return mid
        elif nums[mid] < target:
             left= mid + 1
        else :
             right = mid - 1
    return - 1
nums = [3, 6, 9, 13, 18, 26, 37]
print(binary_search(nums, 26))
print(binary_search(nums, 9))
print(binary_search(nums, 376))
