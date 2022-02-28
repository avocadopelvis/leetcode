# https://leetcode.com/problems/diameter-of-binary-tree/

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        self.length(root)
        return self.diameter
        
    def length(self, root):
        if not root:
            return 0
        
        #traverse through the left & right sub trees
        left = self.length(root.left)
        right = self.length(root.right)
        
        #update the diameter
        self.diameter = max(self.diameter, left+right)
        
        #add 1 for the current node
        return 1 + max(left, right)
      
      
