class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #initialize result as a queue to use appendleft because list has no appendleft
        result = deque()
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
                #insert the children of current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                    
            result.appendleft(currentLevel)
        
        return result
