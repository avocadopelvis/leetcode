# https://leetcode.com/problems/palindrome-linked-list/

# Explanation:
# https://leetcode.com/problems/palindrome-linked-list/discuss/1137027/JS-Python-Java-C%2B%2B-or-Easy-Floyd's-%2B-Reversal-Solution-w-Explanation

# As we know, a palindrome LinkedList will have nodes values that read the same backward or forward. 
# This means that if we divide the LinkedList into two halves, the node values of the first half in the forward direction should be similar to the node values of the second half in the backward direction. 
# As we have been given a Singly LinkedList, we can’t move in the backward direction. To handle this, we will perform the following steps:

# 1. We can use the Fast & Slow pointers method similar to Middle of the LinkedList to find the middle node of the LinkedList.
# 2. Once we have the middle of the LinkedList, we will reverse the second half.
# 3. Then, we will compare the first half with the reversed second half to see if the LinkedList represents a palindrome.

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        prev = None
        
        # find the middle 
        # slow will be in the middle
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # assign prev as the middle (slow)
        # assign the node next to slow as slow
        # prev will point to NULL to break off the first half
        prev, slow, prev.next = slow, slow.next, None
        
        # reversal
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
            
        # send fast back to head (first node)
        # slow is in prev (last node of the original list / first node of the reversed list)
        fast, slow = head, prev
       
        # compare values 
        while slow:
            if fast.val != slow.val:
                return False
            
            # update fast and slow
            fast, slow = fast.next, slow.next
            
        return True
      
      
# The algorithm will have a time complexity of O(N) where N is the number of nodes in the LinkedList.
# The algorithm runs in constant space O(1).


      
     
