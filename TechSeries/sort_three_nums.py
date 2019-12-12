"""
Given a list with 3 unique numbers(1, 2, 3), sort it in linear time.
"""

def sort_nums(nums):
    i = 0
    one_index = 0
    three_index = len(nums) - 1

    while i <= three_index:
        if nums[i] == 1:
            nums[i], nums[one_index] = nums[one_index], nums[i]
            i += 1
            one_index += 1
        elif nums[i] == 2:
            i += 1
        elif nums[i] == 3:
            nums[i], nums[three_index] = nums[three_index], nums[i]
            three_index -= 1
    
    return nums


li = [3, 3, 2, 1, 3, 2, 1]
sort_nums(li) # => [1, 1, 2, 2, 3, 3, 3]
