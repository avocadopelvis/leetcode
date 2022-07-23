# https://leetcode.com/problems/reverse-linked-list/

# 3 pointers prev, current, next
# prev is initially null
# current is the head
# next is next to current

# To reverse:
# current.next is pointed to prev
# prev becomes current
# current becomes next

# we return prev since it's current (head)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            next = current.next
            
            #reversal happens here
            current.next = prev
            prev = current
            current = next
            
        return prev
      
# The time complexity of our algorithm will be O(N) where N is the total number of nodes in the LinkedList.
# We only used constant space, therefore, the space complexity of our algorithm is O(1).
      
      
      
