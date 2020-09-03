"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	# recursive method

	def isValidBST(self, root: TreeNode) -> bool:
		return self.recur(root, float('-inf'), float('inf'))

	def recur(self, node, mini, maxi):
		if not node:
			return True

		if (node.val > mini and node.val < maxi and
				self.recur(node.left, mini, node.val)
				and self.recur(node.right, node.val, maxi)):
			return True
		else:
			return False
	"""
			Complexity Analysis
		
		Time complexity : 0(N)
		O(N) since we visit each node exactly once.
		Space complexity : 
		O(N) since we keep up to the entire tree.

	"""

	# iterative method
	def isValidBST1(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if not root:
			return True

		stack = [(root, float('-inf'), float('inf')), ]
		while stack:
			root, lower, upper = stack.pop()
			if not root:
				continue
			val = root.val
			if val <= lower or val >= upper:
				return False
			stack.append((root.right, val, upper))
			stack.append((root.left, lower, val))
		return True

	"""
				Complexity Analysis

			Time complexity : 0(N)
			O(N) since we visit each node exactly once.
			Space complexity : 
			O(N) since we keep up to the entire tree.

		"""