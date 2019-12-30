
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse_list(self, head):
        if head is None:
            return head

        left = None
        mid = head
        right = mid.next

        while True:
            mid.next = left
            left = mid
            mid = right
            if mid is None: return left
            right = mid.next
