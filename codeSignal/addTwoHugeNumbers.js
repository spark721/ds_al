
// CodeSignal > Interview Practice > Linked Lists
// Easy

/*
You're given 2 huge integers represented by linked lists.
Each linked list element is a number from 0 to 9999
that represents a number with exactly 4 digits.
The represented number might have leading zeros.
Your task is to add up these huge integers
and return the result in the same format.
*/


// Singly-linked lists are already defined with this interface:
// function ListNode(x) {
//   this.value = x;
//   this.next = null;
// }
//
function addTwoHugeNumbers(a, b) {
    let arr1 = getArr(a);
    let arr2 = getArr(b);
    let sumArr = sumTwoArrays(arr1, arr2);
    
    return createList(sumArr);
}

function getArr(list) {
    let arr = [];
    
    while (list) {
        arr.push(list.value);
        list = list.next;
    }
    
    return arr;
}

function sumTwoArrays(arr1, arr2) {
    let arr = [];
    let carry = 0;
    
    while (arr1.length || arr2.length) {
        let v1 = arr1.length ? arr1.pop() : null;
        let v2 = arr2.length ? arr2.pop() : null;
        let sum = v1 + v2;
        
        if (carry) {
            sum += 1;
            carry = 0;
        };
        
        if (sum >= 10000) {
            sum = sum % 10000;
            carry = 1;
        };
        
        arr.unshift(sum);
    }
    
    if (carry) arr.unshift(carry);
    
    return arr;
}

function createList(arr) {
    let list = new ListNode(null);
    let cur = list;
    
    for (let i = 0; i < arr.length; i += 1) {
        cur.next = new ListNode(arr[i]);
        cur = cur.next;
    }
    
    return list.next;
}
