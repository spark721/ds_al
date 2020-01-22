
# LeetCode 665

# Given an array with n integers, 
# your task is to check if it could become non-decreasing by modifying at most 1 element.

# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i(1 <= i < n).

# Example 1:

# Input: [4, 2, 3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

# Example 2:

# Input: [4, 2, 1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        idx = None
        for i in range(len(nums)-1):
            if nums[i] > nums[i + 1]:
                # if there's two tips or more
                if idx is not None:
                    return False
                idx = i
        # if there's no dip
        if idx is None:
            return True
        # if there's only one dip
        if idx == 0:
            return True
        if idx == len(nums) - 2:
            return True
        if nums[idx] <= nums[idx + 2]:
            return True
        if nums[idx - 1] <= nums[idx + 1]:
            return True
        return False