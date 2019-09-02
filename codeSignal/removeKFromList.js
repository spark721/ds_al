
// CodeSignal > Interview Practice > Linked Lists
// Easy

/*
Note: Try to solve this task in O(n) time using O(1) additional space,
where n is the number of elements in the list,
since this is what you'll be asked to do during an interview.

Given a singly linked list of integers l and an integer k,
remove all elements from list l that have a value equal to k.
*/

// Singly-linked lists are already defined with this interface:
// function ListNode(x) {
//   this.value = x;
//   this.next = null;
// }
//
function removeKFromList(l, k) {
    
    let result = new ListNode();
    if (l === null) return l;
    let cur = result;
    
    while (l) {
        if (l.value !== k) {
            cur.next = new ListNode(l.value);
            cur = cur.next;
        }
        l = l.next;
    }
    return result.next;
}

