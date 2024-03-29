
"""
Problem Statement #
Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.

Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

Example 1:

Input: [4, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.
Example 2:

Input: [1, 3, 8, 10, 15], key = 12
Output: 4
Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.
Example 3:

Input: [4, 6, 10], key = 17
Output: -1
Explanation: There is no number greater than or equal to '17' in the given array.
Example 4:

Input: [4, 6, 10], key = -1
Output: 0
Explanation: The smallest number greater than or equal to '-1' is '4' having index '0'.

"""

class Solution:
	def ceiling(self, arr, key):
		start, end = 0, len(arr)-1
		if key <= arr[end]:
			ceiling = arr[end]
		else:
			return -1

		while start<=end:
			mid = start + (end-start)//2
			if arr[mid] == key:
				return mid
			elif arr[mid] > key:
				ceiling = min(ceiling, arr[mid])
				end = mid-1
			else:
				start = mid + 1


		return ceiling

	def flooring(self, arr, key):
		start, end = 0, len(arr)-1
		if key >= arr[start]:
			flooring = arr[start]
		else:
			return -1

		while start<=end:
			mid = start + (end-start)//2
			if arr[mid] == key:
				return mid
			elif arr[mid] > key:
				end = mid-1
			else:
				flooring = max(flooring, arr[mid])
				start = mid + 1

		return flooring


test = Solution()
arr = [1, 3, 8, 10, 15]
key = 12
print(test.ceiling(arr, key))
print(test.flooring(arr, key))