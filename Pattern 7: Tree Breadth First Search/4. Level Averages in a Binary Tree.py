# https://leetcode.com/problems/average-of-levels-in-binary-tree/

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        if not root:
            return result
        
        queue = deque()
        queue.append(root)
        
        while queue:
            levelSize = len(queue)
            levelSum = 0.0 #take 0.0 to get decimal values later
            
            for _ in range(levelSize):
                currentNode = queue.popleft()
                #add the node's value to the running sum
                levelSum += currentNode.val
                #insert the children of current Node to the queue
                if currentNode.left:
                    queue.append(currentNode.left)    
                if currentNode.right:
                    queue.append(currentNode.right)
            
            #append the current level's average to result
            result.append(levelSum/levelSize)
            
        return result

    
