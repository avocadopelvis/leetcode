# https://leetcode.com/problems/merge-k-sorted-lists/

# First check for base cases:
# If lists is empty is empty, return None
# If list has only one element, return it

# Take two list from the lists
# Now Use : (merge two sorted lists) as a function & merge the two list & append it to merged list

# We have to make sure that there are two lists in each case i.e second list should be within the length of lists or else we just return the second list as None


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: #if lists empty
            return None
        
        if len(lists) == 1: #if lists has only 1 list
            return lists[0]
        
        while len(lists) > 1:
            mergedList = []
            
            for i in range(0, len(lists), 2): #taking 2 steps since we're taking 2 lists
                list1 = lists[i]
                list2 = lists[i+1]  if (i+1) < len(lists) else None #to make sure there is a second list
                #merge the two lists
                mergedList.append(self.mergeList(list1, list2))
                
            lists = mergedList
        return lists[0] #0 because there will be only a single merged list
                
    #same as merge two sorted lists
    def mergeList(self, list1, list2):
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
            
        tail.next = list1 or list2 #in case there is still nodes left in one of the list 
        
        return dummy.next
      
      
      
        
