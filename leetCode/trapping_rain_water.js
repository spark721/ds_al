
// LeetCode
// # 42
// Hard

/*

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

*/


const trap = function(a) {
	if (a.length < 3) return 0;

    let count = 0;
    let maxLeft = new Array(a.length).fill(0);
    maxLeft[1] = a[0];

    let maxRight = new Array(a.length).fill(0);
    maxRight[maxRight.length - 2] = a[a.length - 1];

    for (let i = 2; i < maxLeft.length; i += 1) {
    	let curMaxLeft = Math.max(maxLeft[i - 1], a[i - 1]);
    	maxLeft[i] = curMaxLeft;
    };

    for (let i = maxRight.length - 2; i >= 0; i -= 1) {
    	let curMaxRight = Math.max(maxRight[i + 1], a[i + 1]);
    	maxRight[i] = curMaxRight;
    };

    for (let i = 1; i < a.length; i += 1) {
    	let lower = Math.min(maxLeft[i], maxRight[i]);
    	if (lower - a[i] > 0) {
    		count += lower - a[i];
    	};
    };
    return count;
};

