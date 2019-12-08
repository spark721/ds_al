"""
LeetCode
383
Easy

Given an arbitrary ransom note string and 
another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be 
constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Scan thru the mag and create frequency count hash map.
        scan thru ransomNote on each letter
            check against freq count and decrement the value
            return false if the value is not >= 0
        return true
        """
        freq_count = {}
        for c in magazine:
            if freq_count.get(c) is None:
                freq_count[c] = 1
            else:
                freq_count[c] += 1
        
        for c in ransomNote:
            if freq_count.get(c) is None:
                return False
            else:
                freq_count[c] -= 1
                if freq_count[c] < 0: return False
            
        return True
