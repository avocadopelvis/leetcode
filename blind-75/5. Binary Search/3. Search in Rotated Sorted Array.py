# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        
        while l<=r:
            mid = l + (r-l)//2
            
            if nums[mid] == target:
                return mid
            
            # left sorted portion
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]: # if target is between l & mid
                    r = mid - 1
                else:
                    l = mid + 1
            
            # right sorted portion
            else:
                if nums[mid] <= target <= nums[r]: # if target is between mid & r
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return -1
      
      
      
      
      
  
