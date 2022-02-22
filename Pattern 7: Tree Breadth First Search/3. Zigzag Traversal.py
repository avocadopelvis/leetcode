class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        
        queue = deque()
        queue.append(root)
        
        lefttoRight = True
        
        while queue:
            levelSize = len(queue)
            currentLevel = deque() #using queue instead of list because list cannot use appendleft
            
            for _ in range(levelSize):
                currentNode = queue.popleft()
                
                #add the node to the current level based on the traverse direction
                if lefttoRight:
                    currentLevel.append(currentNode.val)
                else:
                    currentLevel.appendleft(currentNode.val) #first [9] then [20, 9] i.e left of 9
                
                #insert the children of the current node in the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                
            result.append(list(currentLevel)) #can remove list and s
            lefttoRight = not lefttoRight
            
        return result
