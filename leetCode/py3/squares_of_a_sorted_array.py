
# LeetCode
# 977
# Easy

# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.


# Example 1:

# Input: [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]

# Example 2:

# Input: [-7, -3, 2, 3, 11]
# Output: [4, 9, 9, 49, 121]


# Note:

#     1 <= A.length <= 10000
#     -10000 <= A[i] <= 10000
#     A is sorted in non-decreasing order.


class Solution:
    def sortedSquares(self, li: List[int]) -> List[int]:
        '''
        split the list into neg and pos
        neg with all values < 0
        pos with all values >= 0
        square everything and reverse the neg list
        two pointer on each list
        compare and push lower value into a result list
        if one of the list is not empty,
        concat the remainder to the end of the result
        '''
        result = list()

        neg = list(filter(lambda n: n < 0, li))
        neg.reverse()
        neg = list(map(lambda n: n ** 2, neg))

        pos = list(filter(lambda n: n >= 0, li))
        pos = list(map(lambda n: n ** 2, pos))

        while len(neg) and len(pos):
            if neg[0] < pos[0]:
                result.append(neg.pop(0))
            else:
                result.append(pos.pop(0))
        
        if len(neg) > 0:
            result += neg
        elif len(pos) > 0:
            result += pos

        return result
