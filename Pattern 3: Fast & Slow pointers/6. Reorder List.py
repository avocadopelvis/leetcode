# https://leetcode.com/problems/reorder-list/

# Find the middle of the list using slow & fast pointer. 
# The second half will start from the node next to the slow node.
# Reverse the second half.
# Merge the elements of the first half with the second half

# Explanation:
# https://www.youtube.com/watch?v=S5bfdUTrKLM

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #find middle node
        slow = head
        fast = head.next
        
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            
        #second half
        second = slow.next #start of second half is next to slow
        
        #reverse second half
        prev = slow.next = None  #slow.next is also None since it is the end of the first half
        current = second
        
        while current:
            next = current.next
            #reversal
            current.next = prev
            prev = current
            current = next
            
        #reorder
        first = head
        second = prev #since prev is now the head of the second half
        
        while second: #taking second since second half might be shorter
            #temp
            tmp1 = first.next
            tmp2 = second.next
            
            #merge
            first.next = second
            second.next = tmp1
            
            #update
            first = tmp1
            second = tmp2
       
# The above algorithm will have a time complexity of O(N) where N is the number of nodes in the LinkedList.
# The algorithm runs in constant space O(1).



