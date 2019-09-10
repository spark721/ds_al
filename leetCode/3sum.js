
// LeetCode > Cisco
// # 15
// Medium


/*

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

*/


const threeSum = function(nums) {
	nums.sort((a, b) => a - b);

	let result = [];
	let target = 0;

	for (let i = 0; i < nums.length - 2; i += 1) {
		let leftIdx = i + 1;
		let rightIdx = nums.length - 1;

		if (i > 0 && nums[i] === nums[i - 1]) continue;
		if (nums[i] > 0) break;

		while (leftIdx < rightIdx) {
			let sum = nums[i] + nums[leftIdx] + nums[rightIdx];

			if (sum === 0) {
				result.push([ nums[i], nums[leftIdx], nums[rightIdx] ]);
				leftIdx += 1;
				rightIdx -= 1;
                while (leftIdx < rightIdx && nums[leftIdx] === nums[leftIdx - 1]) {
					leftIdx += 1;
                };

                while (leftIdx < rightIdx && nums[rightIdx] === nums[rightIdx + 1]) {
                        rightIdx -= 1;
                };
			} else if (sum < 0) {
				leftIdx += 1;
			} else {
				rightIdx -= 1;
			};
		};
	};

	return result;
};


