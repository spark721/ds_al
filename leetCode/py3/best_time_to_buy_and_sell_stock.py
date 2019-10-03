
# LeetCode
# 121
# Easy

# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6), profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.

# Example 2:

# Input: [7, 6, 4, 3, 1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


# import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        single pass with two variables
        init min and max_profit to maxsize and 0
        loop thru the prices
        if min > cur: min = cur
        elif max_profit < cur - min:
            max_profit = cur - min
        return max_profit
        '''
        if len(prices) == 0: return 0
        lowest = max(prices) + 1
        max_profit = 0
        
        for n in prices:
            if lowest > n:
                lowest = n
            elif max_profit < n - lowest:
                max_profit = n - lowest
        
        return max_profit
        
        # min = sys.maxsize
        # max = 0
        
        # for n in prices:
        #     if min > n:
        #         min = n
        #     elif max < n - min:
        #         max = n - min
        
        # return max
