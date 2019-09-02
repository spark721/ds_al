
// CodeSignal > Interview Practice > Linked Lists
// Easy

/*
Asked by Amazon, Facebook
Given a singly linked list of integers, determine whether or not it's a palindrome

Note: Try to solve this task in O(n) time using O(1) additional space,
where n is the number of elements in l,
since this is what you'll be asked to do during an interview.
*/

function ListNode(x) {
	this.value = x;
	this.next = null;
}

function isListPalindrome(l) {
    if (!l.next || l === null) return true;

    let arr = [];

    let node = l;
    
    while (node) {
    	arr.push(node.value);
    	node = node.next;
    }

    let p1 = 0;
    let p2 = arr.length - 1;

    while (p1 <= p2) {
    	if (arr[p1] !== arr[p2]) return false;
    	p1 += 1;
    	p2 -= 1;
    }

    return true;
}
