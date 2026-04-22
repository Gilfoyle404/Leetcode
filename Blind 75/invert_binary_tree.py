"""Problem 19 - Invert Binary Tree
   Link - https://leetcode.com/problems/invert-binary-tree/description/?envType=problem-list-v2&envId=w1thoc57
   
   Question - Given the root of a binary tree, invert the tree, and return its root."""

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root == None:
            return root
        
        root.left,root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root        