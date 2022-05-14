# https://leetcode.com/problems/linked-list-cycle/

# Floyd's Tortoise and Hare Algorithm

# 	2 pointers: slow & fast
# 	fast is 1 step faster than slow	
# 	slow & fast will land in the same node eventually if there is a cycle

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      slow = fast = head

      while fast and fast.next: #if there is no cycle, fast.next will reach NULL
          slow = slow.next
          fast = fast.next.next
          if slow == fast:
              return True

      return False
    
    
    
