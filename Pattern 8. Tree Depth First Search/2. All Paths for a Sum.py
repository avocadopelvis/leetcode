# https://leetcode.com/problems/path-sum-ii/

#DFS + Recursion
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        self.hasPathSum(root, targetSum, [], result)
        return result
        
    def hasPathSum(self, current, targetSum, path, result):
        #if there is no root
        if not current:
            return
        
        #if current node is a leaf & its value is equal to targetSum,  we append the path to result     
        if not current.left and not current.right and current.val == targetSum:
            path.append(current.val)
            result.append(path)
            
        #we add the current node value to the path    
        #recursively call to traverse the left & right sub tree
        self.hasPathSum(current.left, targetSum - current.val, path + [current.val], result)
        self.hasPathSum(current.right, targetSum - current.val, path + [current.val], result
