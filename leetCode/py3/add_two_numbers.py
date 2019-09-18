
# // LeetCode
# // # 2
# // Medium

# /*

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# */

# /*

# init carry and sum to 0
# while at least 1 list exist
# 	add two values and carry
# 	reset carry
# 	if sum >= 10
# 		mod by 10
# 		update carry
# 	create and attach the new node with sum

# */


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(None)
        pointer = result
        carry = 0
        sum = 0
        while l1 or l2:
        	if l1 != None and l2 != None:
        		sum = l1.val + l2.val + carry
        		l1 = l1.next
        		l2 = l2.next
        	elif l1 == None:
        		sum = l2.val + carry
        		l2 = l2.next
        	elif l2 == None:
        		sum = l1.val + carry
        		l1 = l1.next

        	carry = 0
        	if sum >= 10:
        		sum = sum % 10
        		carry = 1

        	pointer.next = ListNode(sum)
        	pointer = pointer.next

        if carry:
            pointer.next = ListNode(1)

        return result.next



