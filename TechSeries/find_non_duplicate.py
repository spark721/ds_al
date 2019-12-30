# Given a list of numbers, find the non-duplicate number
# [4, 3, 2, 4, 1, 3, 2] => 1

class Solution():
    def singleNumber(self, nums):
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for k, v in freq.items():
            if v == 1:
                return k

    
    def singleNumber2(self, nums):
        unique = 0
        for n in nums:
            unique ^= n
        return unique


l = [4, 3, 2, 4, 1, 3, 2]
print(Solution().singleNumber2(l))
