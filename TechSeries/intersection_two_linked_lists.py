
# LeetCode 160

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        calculate the length of both ll
            setup a helper function to calculate it
        place the pointers so both ll will have same remaining length
        traverse through the ll
        if two nodes are identical return the node
        """
        def get_length(head):
            if not head:
                return 0
            return 1 + get_length(head.next)
        
        len_a, len_b = get_length(headA), get_length(headB)
        curr_a, curr_b = headA, headB
        
        if len_a > len_b:
            for _ in range(len_a - len_b):
                curr_a = curr_a.next
        else:
            for _ in range(len_b - len_a):
                curr_b = curr_b.next

        while curr_a is not None:
            if curr_a == curr_b:
                return curr_a
            curr_a, curr_b = curr_a.next, curr_b.next
