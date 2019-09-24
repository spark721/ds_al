
# LeetCode
# 15
# Medium

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
		'''
		sort the list
		loop thru the list
			two pointer approach
			pointer1 - i + 1
			pointer2 - list[-1]

			while pointer1 <= pointer2

				if target < (el + pointer1 + pointer2)
					move pointer2 to left
				if target > (el + pointer1 + pointer2)
					move pointer1 to right
				if target == (el + pointer1 + pointer2)
					push into result list
		return result list
		'''
		t = 0
        res = []
        li = sorted(nums)
        
        for i in range(len(li) - 2):
            p1 = i + 1
            p2 = len(li) - 1
            
            if i > 0 and li[i] == li[i - 1]: continue
            
            if li[i] > 0: break

            while p1 < p2:
                el, left, right = li[i], li[p1], li[p2]
                cur = [el, left, right]
                cur_sum = el + left + right
                
                if t == cur_sum:
                    res.append(cur)
                    p1 += 1
                    p2 -= 1
                    
                    while p1 < p2 and li[p1] == li[p1 - 1]: p1 += 1
                    while p1 < p2 and li[p2] == li[p2 + 1]: p2 -= 1
                    
                elif t > cur_sum:
                    p1 += 1
                elif t < cur_sum:
                    p2 -= 1

        return res
