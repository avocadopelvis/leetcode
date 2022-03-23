# https://leetcode.com/problems/minimum-depth-of-binary-tree/

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        #DFS RECURSIVE
        
        #if both left and right node are not empty
        # if root.left and root.right:
        #     return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        # #if one of the nodes is empty
        # else:
        #     return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        
        #BFS
        minDepth = 0
        queue = deque()
        queue.append(root)
        
        while queue:
            minDepth += 1
            levelSize = len(queue)
            
            for _ in range(levelSize):
                currentNode = queue.popleft()
                
                #check if this is a leaf node
                if not currentNode.left and not currentNode.right:
                    return minDepth
                
                #insert the children of current node to the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                    
