"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.



Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
"""
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def maxLevelSum(self, root: Optional[TreeNode]) -> int:
		maxi = {}
		level = 0
		if not root:
			return 0
		queue = deque()
		queue.append(root)

		while queue:
			level += 1
			lvl = len(queue)
			current_sum = 0
			for _ in range(lvl):
				current_node = queue.popleft()
				current_sum += current_node.val
				if current_node.left:
					queue.append(current_node.left)
				if current_node.right:
					queue.append(current_node.right)
			maxi[level] = current_sum
		out = 0
		max_ = max(maxi.values())
		for key, val in maxi.items():
			if val == max_:
				return key
