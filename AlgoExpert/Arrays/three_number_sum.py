"""
Arrays - 2/11
Medium

Write a function that takes in a non-empty array of distinct integers and 
an integer representing a target sum. The function should find 
all triplets in the array that sum up to the target sum and 
return a two-dimensional array of all these triplets. 
The numbers in each triplet should be ordered in ascending order, 
and the triplets themselves should be ordered in ascending order 
with respect to the numbers they hold. 
If no three numbers sum up to the target sum, 
the function should return an empty array.
"""

def threeNumberSum(arr, t):
	res = []
	arr.sort()

	for i in range(len(arr) - 2):
		num = arr[i]
		left = i + 1
		right = len(arr) - 1

		while left < right:
			current_sum = num + arr[left] + arr[right]
			if current_sum == t:
				res.append([num, arr[left], arr[right]])
				left += 1
				right -= 1
			elif current_sum < t:
				left += 1
			elif current_sum > t:
				right -= 1

	return res
