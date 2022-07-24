# https://leetcode.com/problems/rotate-list/

# Explanation:
# https://leetcode.com/problems/rotate-list/discuss/348197/96-faster-Simple-python-solution-with-explanation
# comments here might be better

# the basic idea is to make the linked list into a circular linked list and break the list off at a certain point to get the required result

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # initialize last as head
        last = head
        # initialize lenght of the list as 1
        l = 1
        
        # get the length of the list and the last node in the list
        while last.next:
            last = last.next
            l += 1
        
        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        # Example: In 0->1->2, and k = 4
        #          k = k % l = 1 
        # which would result in: 2->0->1
        # the same as k = 4
        k = k % l
        
        # by setting the last node to point to head, 
        # the list is now a circular linked list
        last.next = head
        
        # next thing to do is break the list off at a certain point
        # so that we can get the required result
        
        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)
        tempNode = head
        for _ in range(l-k-1):
            tempNode = tempNode.next
        
        # Get the node next to tempNode and then set tempNode.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = tempNode.next
        tempNode.next = None
        
        return answer

# The time complexity of our algorithm will be O(N) where N is the total number of nodes in the LinkedList.
# We only used constant space, therefore, the space complexity of our algorithm is O(1).

