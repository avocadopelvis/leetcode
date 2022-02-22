class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level, maxLevel = 0, 1
        maxSum = float('-inf')
        
        queue = deque()
        queue.append(root)
        
        while queue:
            levelSum = 0
            levelSize = len(queue)
            
            for _ in range(levelSize):
                currentNode = queue.popleft()
                
                levelSum += currentNode.val
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            
            level += 1
            
            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = level
