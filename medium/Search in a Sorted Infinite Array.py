"""
Problem Statement #
Given an infinite sorted array (or an array with unknown size), find if a given number ‘key’ is present in the array. Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Since it is not possible to define an array with infinite (unknown) size, you will be provided with an interface ArrayReader to read elements of the array. ArrayReader.get(index) will return the number at index; if the array’s size is smaller than the index, it will return Integer.MAX_VALUE.

Example 1:

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
Output: 6
Explanation: The key is present at index '6' in the array.
Example 2:

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 11
Output: -1
Explanation: The key is not present in the array.
Example 3:

Input: [1, 3, 8, 10, 15], key = 15
Output: 4
Explanation: The key is present at index '4' in the array.
Example 4:

Input: [1, 3, 8, 10, 15], key = 200
Output: -1
Explanation: The key is not present in the array.

"""
class ArrayReaders:
	def __init__(self, arr):
		self.arr = arr

	def get(self, index):
		if index>= len(self.arr):
			return float('inf')
		return self.arr[index]


class Solution:
	def search_in_infinite_array(self, reader, key):
		start, end = 0, len(reader.arr)-1
		if reader.get(end)==float('inf'):
			return -1
		while start <= end:
			mid = start + (end-start)//2

			if reader.arr[mid] == key:
				return mid
			elif reader.arr[mid] > key:
				end = mid-1
			else:
				start = mid +1
		return -1


test = Solution()
arr = [24,6,8,10,12,14,16,18,20,22,24,26,28,30]
arr1 = [1,3,8,10,15]
reader = ArrayReaders(arr1)
print(test.search_in_infinite_array(reader, 200))

test = Solution()