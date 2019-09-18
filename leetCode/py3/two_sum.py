
# // LeetCode
# // # 1
# // Easy

# /*

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# */

# /*

# create obj key of element and value of index
# calculate the difference of element from target
# look up the obj and check the value

# */

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for i, cur in enumerate(nums):
            dif = target - cur
            if dif in d and d[dif] != i:
                return [ d[dif], i ]
            elif dif not in d:
                d[cur] = i
                
