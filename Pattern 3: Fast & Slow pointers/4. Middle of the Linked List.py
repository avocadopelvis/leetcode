# https://leetcode.com/problems/middle-of-the-linked-list/

# Solution:
# https://leetcode.com/problems/middle-of-the-linked-list/solution/
# Approach 2: Fast and Slow Pointer

# When traversing the list with a pointer "slow", make another pointer "fast" that traverses twice as fast. 
# When "fast" reaches the end of the list, "slow" must be in the middle.

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is in the middle
        return slow
      
      
# Complexity Analysis:
# Time Complexity: O(N), where N is the number of nodes in the given list.
# Space Complexity: O(1), the space used by slow and fast.
