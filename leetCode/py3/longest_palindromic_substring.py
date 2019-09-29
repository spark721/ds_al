
# LeetCode
# 5
# Medium

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:

# Input: "cbbd"
# Output: "bb"



class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        loop thru the string
        on each char, check both left and right
        if equal, fan out
        '''
        if s == '' or len(s) == 1: return s
        if s == s[::-1]: return s

        longest = ''
        for i in range(len(s)):
            for n in range(2):
                left = i
                right = i + n

                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1

                if right - left - 1 > len(longest):
                    longest = s[left + 1 : right]

        return longest

