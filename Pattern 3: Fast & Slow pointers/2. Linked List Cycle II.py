# https://leetcode.com/problems/linked-list-cycle-ii/

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
                
        #  # if not (fast and fast.next): return None
        else:
            return None
        
        while head != slow:
            # if head and slow start to move at the same time, they will meet at the start of the cycle
            head = head.next
            slow = slow.next
            
        return head
      
# As we know, finding the cycle in a LinkedList with N nodes and also finding the length of the cycle requires O(N).
# Also, as we saw in the above algorithm, we will need O(N) to find the start of the cycle. 
# Therefore, the overall time complexity of our algorithm will be O(N).

# The algorithm runs in constant space O(1).

