# https://leetcode.com/problems/binary-tree-paths/

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        if not root:
            return result
        
        self.hasPath(root, "", result)
        return result
        
    def hasPath(self, root, path, result):
        #if current node is a leaf, we append its value to result
        if not root.left and not root.right:
            result.append(path + str(root.val))
        
        #check for left and right sub trees
        if root.left:
            self.hasPath(root.left, path + str(root.val) + '->', result)
        if root.right:
            self.hasPath(root.right, path + str(root.val) + '->', result)
            
            
