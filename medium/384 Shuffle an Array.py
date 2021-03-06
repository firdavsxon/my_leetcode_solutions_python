"""
Given an integer array nums, design an algorithm to randomly shuffle the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.


Example 1:

Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must be equally likely to be returned. Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

"""
from typing import List


class Solution:

	def __init__(self, nums: List[int]):
		self.nums = nums
		self.shuffling = nums[:]

	def reset(self) -> List[int]:
		"""
		Resets the array to its original configuration and return it.
		"""
		return self.nums

	def shuffle(self) -> List[int]:
		"""
		Returns a random shuffling of the array.
		"""
		import random
		random.shuffle(self.shuffling)
		return self.shuffling

# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3]
obj = Solution(nums)
print(obj.shuffle(), end =' ')
print(obj.reset(), end = ' ')
print(obj.shuffle(), end= ' ')