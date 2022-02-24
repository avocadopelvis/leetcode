# https://leetcode.com/problems/path-sum/

'''
Problem Statement 
Given a binary tree and a number ‘S’, 
find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
'''

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        #if current node is a leaf and its value is equal to targetSum, we've found a path
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        #recursively call to traverse the left & right sub tree
        #it will return True if any of the two recursove calls returns True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        
