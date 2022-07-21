# https://leetcode.com/problems/minimum-absolute-difference/

# Explanation:
# https://leetcode.com/problems/minimum-absolute-difference/solution/

# Approach 1: Sort + 2 Traversals

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # sort the array
        arr.sort()
        res = []
        
        # initialize minimum difference as a huge integer in order not 
        # to miss the absolute difference of the first pair. 
        min_dif = float('inf')
        
        # traverse the sorted array and calcalute the minimum absolute difference.
        for i in range(len(arr) - 1):
            min_dif = min(min_dif, arr[i+1] - arr[i])
            
        # traverse the sorted array and check every pair again
        # if the absolute difference equals the minimum difference, 
        # add this pair to res 
        for i in range(len(arr) - 1): 
            if arr[i+1] - arr[i] == min_dif:
                res.append([arr[i], arr[i+1]])
                
        return res
      
# Time complexity: O(n⋅logn)
# Space complexity: O(logn) or O(n)

# Approach 2: Sort + 1 Traversal 

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # sort the array
        arr.sort()
        res = []
        
        # initialize minimum difference as a huge integer in order not 
        # to miss the absolute difference of the first pair. 
        min_dif = float('inf')
        
        # traverse the sorted array 
        for i in range(len(arr) - 1):
            
            curr_dif = arr[i+1] - arr[i]
            
            # if curr_dif equals min_dif, add this pair to res
            if curr_dif == min_dif:
                res.append([arr[i], arr[i+1]])
            # if curr_dif is less than min_dif, discard all pairs in res and add current pair to res
            # update min_dif
            elif curr_dif < min_dif:
                res = [[arr[i], arr[i+1]]]
                min_dif = curr_dif
            # if curr_dif is greater than min_dif, we just go ahead
            
        return res
      
# Time complexity: O(n⋅logn)
# Space complexity: O(n)
