# https://leetcode.com/problems/reverse-linked-list-ii/

# EXPLANATION:
# https://www.youtube.com/watch?v=RF_M9tX4Eag

# find the linked list [left, right], reverse it, then connect left with right+1, connect right with left-1

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # dummy node pointing to head
        # it will be useful later for returning head
        dummy = ListNode(0, head)
        
        # initially leftPrev is on dummy
        leftPrev, curr = dummy, head
        
        # iterate until current is on left and leftPrev is on node before left
        for _ in range(left - 1):
            leftPrev = curr
            curr = curr.next
            
        # currently, curr is on left and leftPrev is on the node before left
        
        # reverse the links from left to right
        prev = None
        for _ in range(right - left + 1):
            tmp = curr.next
            
            # reversal
            curr.next = prev
            prev = curr
            curr = tmp
            
        # currently, curr is on the node next to right and prev is on right
        
        # update pointers
        
        # leftPrev.next points to left and we want left.next to point to curr (node next to right)
        leftPrev.next.next = curr
        leftPrev.next = prev
        
        return dummy.next
      
      
# The time complexity of our algorithm will be O(N) where N is the total number of nodes in the LinkedList.
# We only used constant space, therefore, the space complexity of our algorithm is O(1).

