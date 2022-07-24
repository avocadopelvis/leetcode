# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Explanation:
# https://www.youtube.com/watch?v=1UOPsfP85V4
  

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # dummy node pointing to head
        # it will be useful later for returning head
        dummy = ListNode(0, head)
        # groupPrev is the node before a new group
        # we need this to point towards the new start of the reversed group
        groupPrev = dummy
        
        while True:
            # get the kth node
            kth = self.getKth(groupPrev, k)
            # if kth does not exist, it means that the number of nodes is not a multiple of k
            if not kth:
                break
            
            # node right after the group
            groupNext = kth.next
            
            # reverse group
            
            # originally it should be NULL but in order to connect with another group
            # we will use kth.next
            prev = kth.next 
            curr = groupPrev.next # groupPrev.next is the 1st node in a group
            
            # since groupNext marks the end
            while curr != groupNext:
                tmp1 = curr.next
                curr.next = prev
                prev = curr
                curr = tmp1
                
            # reverse ends
            
            # before reversal, groupPrev.next is the first node in our group 
            tmp2 = groupPrev.next 
            # after reversal, we want kth to be the first node in our group
            groupPrev.next = kth
            # update groupPrev for the next group:
            # after reversal, the first node is the last node 
            # which would be the node right before the new group (groupPrev)
            groupPrev = tmp2
            
        # dummy.next is the head
        return dummy.next
            
            
    # helper function to help us get the kth node
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        # curr will be on the kth node
        return curr
      
# The time complexity of our algorithm will be O(N) where N is the total number of nodes in the LinkedList.
# We only used constant space, therefore, the space complexity of our algorithm is O(1).
   
