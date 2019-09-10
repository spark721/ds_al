
// LeetCode
// # 438
// Medium


/*

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

*/


const findAnagrams = function(s, p) {
	let result = [];
    let sCount = new Array(26).fill(0);
    let pCount = new Array(26).fill(0);
    const aCode = 'a'.charCodeAt();

    // create char frequency count array of p
    [...p].forEach( char => {
    	pCount[ char.charCodeAt() - aCode ] += 1;
    });


    [...s].forEach( (char, i) => {
    	if (i >= p.length) {
    		let oldChar = s[ i - p.length ];
    		sCount[ oldChar.charCodeAt() - aCode ] -= 1;
    	};

    	sCount[ char.charCodeAt() - aCode ] += 1;

    	if (sCount.join() === pCount.join()) {
    		let startIdx = i + 1 - p.length;
    		result.push(startIdx);
    	};
    });

    return result;
};

