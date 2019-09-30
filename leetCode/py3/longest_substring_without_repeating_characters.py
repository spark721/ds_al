
# LeetCode
# 3
# Medium

# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        if len(s) == 1, return 1
        init cur_sub and long_sub to empty''
        loop thru the s with each char
        if char is not in cur_sub
            add char to cur_sub
            compare the length of cur_sub and long_sub
            update long_sub if cur_sub is longer
        else
            slice cur_sub with index of char + 1 and add char
        return long_sub length
        '''
        if len(s) == 1: return 1
        cur_sub, long_sub = '', ''

        for char in s:
            if char not in cur_sub:
                cur_sub += char
                if len(cur_sub) > len(long_sub):
                    long_sub = cur_sub
            else:
                char_idx = cur_sub.index(char)
                cur_sub = cur_sub[ char_idx + 1 :] + char
        
        return len(long_sub)
