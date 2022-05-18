# leetcode.com/problems/maximum-depth-of-binary-tree/

# • Recursive Depth First Search:

# Find the max depth of the subtrees if the root is not empty.
# Time complexity: O(n) since we're traversing the entire tree.

# • Iterative Depth First Search:

# Use Stack.
# Keep track of node & depth.
# Traverse through the tree in preorder.

# • Iterative Breadth First Search:

# Use Queue.
# Traverse the entire level & add the next level.
# Keep track of the level (count the levels)


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #recursive DFS
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) #1 is for root
        
        #iterative DFS
#         stack = [[root, 1]]
#         res = 0
        
#         while stack: #if root is null then this won't run
#             node, depth = stack.pop()
            
#             if node:
#                 res = max(res, depth)
#                 stack.append([node.left, 1+depth])
#                 stack.append([node.right, 1+depth])
#         return res
                 
        #iterative BFS
#         if not root:
#             return 0
        
#         queue = deque([root])
#         level = 0
        
#         while queue:
#             level += 1
#             for _ in range(len(queue)):
#                 node = queue.popleft()

#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#         return level




