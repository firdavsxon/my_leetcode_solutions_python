"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [1,2]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up:

Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> Optional[List[int]]:

        if root.left:
            self.inorderTraversal(root.left)
        print(root.val, end=' ')
        if root.right:
            self.inorderTraversal(root.right)





def main():
    root1 = TreeNode(1)
    # root1.left = TreeNode(1)
    root1.right = TreeNode(2)
    # root1.right.next = TreeNode(8)
    # root1.next.next.next = TreeNode(4)
    # root1.next.next.next.next = TreeNode(5)
    # root1.next.next.next.next.next = TreeNode(6)
    # root1.next.next.next.next.next.next = TreeNode(7)
    # root1.next.next.next.next.next.next.next = TreeNode(8)

    test = Solution()

    print(test.inorderTraversal(root1))


main()
