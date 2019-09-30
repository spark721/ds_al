
# LeetCode
# 55
# Medium

# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# Example 1:

# Input: [2, 3, 1, 1, 4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:

# Input: [3, 2, 1, 0, 4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        init max_jump = nums[0]
        loop thru the nums list
        if i > max_jump, return false
        compare i + cur and max_jump
        update the max_jump with bigger value
        return max_jump >= len(nums) - 1
        '''
        if len(nums) == 1: return True

        max_jump = 0
        
        for i, n in enumerate(nums):
            if i > max_jump: return False
            if i < len(nums) - 1:
                max_jump = max( i + n, max_jump )
        
        return max_jump >= len(nums) - 1
