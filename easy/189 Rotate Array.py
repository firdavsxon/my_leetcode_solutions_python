"""
Given an array, rotate the array to the right by k steps,
where k is non-negative.

Follow up:

Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0

"""

from typing import List


class Solution:
	def rotate(self, nums: List[int], k: int):
		k=k%len(nums)
		self.reverse(nums,0, len(nums)-1)
		self.reverse(nums, 0, k-1)
		self.reverse(nums, k, len(nums)-1)
		return nums

	def reverse(self, list, start, end):
		while start<end:
			list[start], list[end]= list[end], list[start]
			start += 1
			end -= 1

def rot(nums, k):
	k%= len(nums)
	nums[:]=nums[-k:]+nums[:-k]
	return nums

def rot2(nums, k):
	a = list(nums)
	for i in range(len(nums)):
		nums[i] = a[(i-k)%len(nums)]
	return nums

test = Solution()
print(test.rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(test.rotate([-1,-100,3,99], 2))
print(rot2([1, 2, 3, 4, 5, 6, 7], 3))