
// LeetCode
// # 560
// Medium

/*

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

*/


const subarraySum = function(nums, k) {
    let map = new Map();
    map.set(0, 1);

    let sum = 0;
    let count = 0;

    nums.forEach( n => {
    	sum += n;
    	
    	if (map.get(sum - k)) {
    		count += map.get(sum - k);
    	};

    	if (map.get(sum)) {
    		map.set(sum, map.get(sum) + 1);
    	} else {
    		map.set(sum, 1);
    	};
    });

    return count;
};



// [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]