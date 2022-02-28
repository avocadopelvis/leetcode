# https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = float('-inf')
        self.pathSum(root)
        return self.maxSum
        
    def pathSum(self, current):
        if not current:
            return 0
        
        #only add positive contributions
        left = max(0, self.pathSum(current.left))
        right = max(0, self.pathSum(current.right))
        
        self.maxSum = max(self.maxSum, left + right + current.val) 
        
        return current.val + max(left, right)
      
      
