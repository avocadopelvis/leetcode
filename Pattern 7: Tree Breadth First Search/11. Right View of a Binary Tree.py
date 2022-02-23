# https://leetcode.com/problems/binary-tree-right-side-view/

'''
Right View of a Binary Tree (easy)

Given a binary tree, return an array containing nodes in its right view. 
The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
'''
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        
        queue = deque([root])
    
        while queue:
            levelSize = len(queue)
            
            for i in range(levelSize):
                currentNode = queue.popleft()
                #right side node will always be the last node in each level
                #if it is the last node of this level, add it to result
                if i == levelSize - 1:
                    result.append(currentNode.val)
                    
                #insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        return result
