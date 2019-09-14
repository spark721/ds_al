
// LeetCode
// # 49
// Medium

/*

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    All inputs will be in lowercase.
    The order of your output does not matter.

*/

/*

	scan through the input array
	split > sort > join each word
	check object if a key of the sorted word exist
		if yes, push the original word into the value array
		if no, init value as array with the original word
	return Object.values of object

*/


var groupAnagrams = function(a) {
	if (!Array.isArray(a)) throw new TypeError("invalid input type.");
	if (a.length === 0) return [];

    let obj = {};

    a.forEach( w => {
    	let key = w.split('').sort().join('');
        
    	if (obj[key]) {
    		obj[key].push(w);
    	} else {
    		obj[key] = [ w ];
    	};
    });

    return Object.values(obj);
};


























