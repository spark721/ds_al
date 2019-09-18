
// LeetCode
// # 283
// Medium


/*

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

*/


var moveZeroes = function(a) {
    let count = 0;
    let i = 0;
    
    while (i < a.length) {
        if (a[i] !== 0) {
            a[count] = a[i];
            count += 1;
        }
        i += 1;
    }
    
    if (count > 0) {
        while (count < a.length) {
            a[count] = 0;
            count += 1;
        }
    }
    
    return a;
};