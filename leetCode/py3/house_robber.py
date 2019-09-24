
# LeetCode
# 198
# Easy

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

# Example 2:

# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.

class Solution:
    def rob(self, nums: List[int]) -> int:
    	'''
    	validate input
    		if empty list, return 0
    		if only 1 in list, return nums[0]

    	init result list with nums[0]

    	while len(result) < len(nums)
    		if i < 2 append max of two
    		else
    			if nums[i] + res[i - 2] > res[i - 1]
    				append
    			else
    				repeat res[i - 1]

    	return res[-1]
    	'''
    	if len(nums) == 0: return 0
    	if len(nums) == 1: return nums[0]

    	res = [ nums[0] ]

    	i = 1
    	while len(res) < len(nums):
    		if i < 2:
    			res.append(max([ nums[0], nums[1] ]))
    		elif nums[i] + res[i - 2] > res[i - 1]:
    			res.append(nums[i] + res[i - 2])
    		else:
    			res.append(res[-1])
    		i += 1

    	return res[-1]
