
# LeetCode
# 17
# Medium

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].



class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        closure recursive approach
        
        init an empty res list
		set up a method that recursively call that takes idx and prev_str
		if prev_str and input are same length, return
		iterate thru d[digits[idx]]
		for every char
			new_str = prev_str + char
			recursively call with idx + 1 and new_str
        return res

        '''
        res = []
        if not digits: return res

        dic = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        }

        def add_chars(idx, prev_str):
        	if len(prev_str) == len(digits):
        		res.append(prev_str)
        		return

        	char_set = dic[ digits[idx] ]
        	
        	for char in char_set:
        		new_str = prev_str + char
        		add_chars(idx + 1, new_str)

        add_chars(0, '')

        return res
