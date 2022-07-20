# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            
            mid = start + (end-start)//2
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        
        return -1
      
     
# Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(log N) 
# where N is the total elements in the given array.

# The algorithm runs in constant space O(1).
