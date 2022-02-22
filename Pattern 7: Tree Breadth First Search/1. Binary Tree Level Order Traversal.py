class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
       #from collections import deque
        
        result = []
        if not root:
            return result
        
        queue = deque()
        queue.append(root)
        
        while queue:
            levelSize = len(queue)
            currentLevel = []
            
            for _ in range(levelSize):
                currentNode = queue.popleft()
                #add node to the current level
                currentLevel.append(currentNode.val)
                
                #insert children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                    
            result.append(currentLevel)
                    
        return result
