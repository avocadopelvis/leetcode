# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

'''
Problem Statement 
Given a binary tree, connect each node with its level order successor. 
The last node of each level should point to a null node.
'''

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            currentNode = queue.popleft()

            if currentNode.left and currentNode.right:
                #left to right
                currentNode.left.next = currentNode.right
                
                #to point a right child node to a left child node of another node
                if currentNode.next:
                    currentNode.right.next = currentNode.next.left
                
                #since it is a perfect binary tree, no need to check 
                queue.append(currentNode.left)
                queue.append(currentNode.right)

        return root
