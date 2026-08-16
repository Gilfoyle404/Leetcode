"""Problem 19 - Invert Binary Tree
   Link - https://leetcode.com/problems/invert-binary-tree/description/?envType=problem-list-v2&envId=w1thoc57
   
   Question - Given the root of a binary tree, return its maximum depth.A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node."""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        