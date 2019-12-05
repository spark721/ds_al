"""
Arrays - 1/11
Easy

Write a function that takes in a non-empty array of distinct integers and 
an integer representing a target sum. 
If any two numbers in the input array sum up to the target sum, 
the function should return them in an array. 
If no two numbers sum up to the target sum, 
the function should return an empty array. 
Assume that there will be at most one pair of numbers 
summing up to the target sum.
"""

def twoNumberSum(array, target):
    # Write your code here.
	s = set()

	for n in array:
		if n in s:
			return [target - n, n]
		else:
			s.add(target - n)

	return []
