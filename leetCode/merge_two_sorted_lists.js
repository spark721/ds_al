
// LeetCode
// # 21
// Easy

/*

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

*/



var mergeTwoLists = function(l1, l2) {
    let res = new ListNode();
    let cur = res;
    
    while (l1 || l2) {
        if (l1 === null) {
            cur.next = l2;
            l2 = l2.next;
            
        } else if (l2 === null) {
            cur.next = l1;
            l1 = l1.next;
            
        } else if (l1.val <= l2.val) {
            cur.next = l1;
            l1 = l1.next;
            
        } else {
            cur.next = l2;
            l2 = l2.next;
            
        }
        cur = cur.next;
        
    }
    
    return res.next;
};