# https://leetcode.com/problems/invert-binary-tree/

# Use recursion.

# If the root is not null, swap its left child to the right & vice versa.
# Now call the function again.

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # if root:
        #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root
        
        if not root:
            return None
        
        #swap the children
        # tmp = root.left #temporarily store the left since it's being shifted
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
            
        return root
      
      
