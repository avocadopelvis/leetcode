# https://leetcode.com/problems/odd-even-linked-list/

# Solution:
# https://leetcode.com/problems/odd-even-linked-list/discuss/133345/With-detailed-explanation-or-Python

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        odd = head
        even = head.next
        # eHead is the head of the even node list
        eHead = even
        
        # loop won't run if there's only one node in the linked list
        while even and even.next:
            # connect the current odd node with the next odd node
            odd.next = odd.next.next
            # connect the current even node with the next even node
            even.next = even.next.next
            
            # update the odd and even node
            odd = odd.next
            even = even.next
            
        # currently "odd" is the last node of the odd node list
        # so we connect it with eHead (the head of the even node list)
        odd.next = eHead
        
        return head
      
# The time complexity of our algorithm will be O(N) where N is the total number of nodes in the LinkedList.
# We only used constant space, therefore, the space complexity of our algorithm is O(1).


      
