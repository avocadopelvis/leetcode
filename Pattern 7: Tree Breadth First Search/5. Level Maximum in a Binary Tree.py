# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

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
            level += 1
            levelSum = 0
            levelSize = len(queue)
            
            for _ in range(levelSize):
                currentNode = queue.popleft()
                levelSum += currentNode.val
                
                # insert children of current node
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
             
            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = level

        return maxLevel
                
            
