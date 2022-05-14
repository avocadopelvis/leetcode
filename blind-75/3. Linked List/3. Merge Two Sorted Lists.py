# https://leetcode.com/problems/merge-two-sorted-lists/

# Use a dummy linkedlist
# compare values of list1 & list2 and attach at the end of dummy (tail.next)
	
# Since one of the sorted lists might be longer than the other, there might be nodes remaining which are not compared, so we check to see if any nodes are remaining & attach them to the merged sorted list


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
            
        tail.next = list1 or list2 #since one of the list could be longer than the other
        return dummy.next #because the sorted list is connected to the dummy 
      
      
      
