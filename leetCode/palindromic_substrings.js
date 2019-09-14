
// LeetCode
// # 647
// Medium

/*

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

 

Note:

    The input string length won't exceed 1000.

*/

/*

init count
scan thru the input string
nested loop with only 2 rounds (index 0 & 1)
	if s[i] === s[i + j] count += 1
		init left (i - 1) and right (j + 1)
		while (
			left and right are within the range 
			s[left] === s[right]
			)
			count += 1, left -=1, right += 1
return count

*/


var countSubstrings = function(s) {
    if (typeof s !== "string") throw new TypeError("invalid input");
    if (s.length === 0) return 0;

    let count = 0;

    for (let i = 0; i < s.length; i += 1) {
    	for (let n = 0; n < 2; n += 1) {
    		if (s[i] === s[i + n]) {
    			count += 1;

    			let left = i - 1;
	    		let right = i + n + 1;
	    		while (
	    			(left >= 0 && right < s.length) &&
	    			s[left] === s[right]
	    			) {
	    			count += 1;
	    			left -=1;
	    			right += 1;
	    		};
    		};
    	};
    };

    return count;
};

























