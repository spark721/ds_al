
# LeetCode
# 56
# Medium

# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        validate input: if len(intervals) == 0: return []
        sort the list
        init result list with sorted[0]

        loop through sorted starting at idx 1
        if left of sorted[i] <= right of result[-1] AND 
            right of sorted[i] > right of result[-1]:
            update last right of result
        else if left of sorted[i] > right of result[-1]:
            append sorted[i] to the result

        return result
        '''
        if len(intervals) == 0: return []

        li = sorted(intervals)
        res = [ li[0] ]

        for i in range(1, len(li)):
            if li[i][0] <= res[-1][1] and li[i][1] > res[-1][1]:
                res[-1][1] = li[i][1]
            elif li[i][0] > res[-1][1]:
                res.append(li[i])

        return res
