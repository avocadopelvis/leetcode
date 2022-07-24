# https://leetcode.com/problems/swap-nodes-in-pairs/submissions/

# Solution:
# https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11019/7-8-lines-C%2B%2B-Python-Ruby

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev is the previous node
        # since head doesn't have a previous node, a dummy node is used
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next and prev.next.next:
            # a & b are the two adjacent nodes that we want to swap
            a = prev.next
            b = a.next
            
            # To go from prev -> a -> b -> b.next to prev -> b -> a -> b.next
            # we need to change those three references
            # Instead of thinking about in what order to change them, just change all three at once
            
            # swap
            prev.next, b.next, a.next = b, a, b.next
            
            # update prev for next pair
            prev = a # since a is now the node before the new pair
        
        return dummy.next
            
        
        
        
