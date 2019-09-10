
// LeetCode
// # 5
// Medium


/*

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

*/


const longestPalindrome = function(s) {
    if (!s || s.length === 1) return s;
    let longest = '';

    if (s[0] === s[s.length - 1]) {
		if (isPalindrome(s)) return s;
    }

    for (let i = 0; i < s.length; i += 1) {
    	for (let n = i; n < s.length; n += 1) {
    		if (s[i] === s[n]) {
    			let sub = s.slice(i, n + 1);
    			if (isPalindrome(sub) && sub.length > longest.length) {
    				longest = sub;
    			};
    		};
    	};
    };

    return longest;
};


const isPalindrome = (s) => {
  let i = 0;
  let n = s.length - 1;
  
  while (i < n) {
    i += 1;
    n -= 1;

    if (s[i] !== s[n]) return false;
  };
  
  return true;
};


