"""
LeetCode
406
Medium

Suppose you have a random list of people standing in a queue. 
Each person is described by a pair of integers (h, k), 
where h is the height of the person and 
k is the number of people in front of this person 
who have a height greater than or equal to h. 
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        sort input by the h(dsc) first then by k (asc).
        for each pair, perform insertion sort.
            insert the pair at k index.
        """
        res = []

        sorted_by_h = sorted(people, key = lambda p: ( -p[0], p[1] ))
        # this sorting is O(n log n)

        for p in sorted_by_h: # O(n)
            res.insert(p[1], p) # O(n)
        
        return res

        # Time complexity: O(n^2)
        # Space: O(n)
