
// LeetCode
// # 23
// Hard

/*

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

*/

/*

while input array.length > 1
    shift first 2 lists,
    pass to helper func mergeTwoLists
    push the return from helper func back into input array

return input[0]

*/




var mergeKLists = function(a) {
    if (!Array.isArray(a)) throw new TypeError('invalid input');
    if (a.length === 0) return null;

    while (a.length > 1) {
        // shift off first two lists
        let l1 = a.shift();
        let l2 = a.shift();

        // pass two lists to helper func and store the result
        let merged = mergeTwoLists(l1, l2);

        // push the merged list back into the input array
        a.push(merged);

        // by doing so,
        // it will keep remove 2 from front > merge into 1 > push into the back
    };

    return a[0];
};



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
