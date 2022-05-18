# https://leetcode.com/problems/same-tree/submissions/
  
# Use recursive DFS.
# Cases:
# • If root node of both trees are null then True (identical)
# • If root node of even one of the trees is null then False

# • If none of the above two cases, then the values have to be equal to be True.
# • Then proceed to use recursion for the left & right nodes of both trees.

# Time complexity is O(p + q) i.e size of both trees added together because worse case we have to iterate through every node in both trees.


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
        #shorter 
        # if p and q:
        #     return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # return p is q #True if p==None and q==None else False.
        
        
