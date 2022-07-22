# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l<r:
            
            while l<r and nums[l] == nums[l+1]:
                l += 1
            while l<r and nums[r] == nums[r-1]:
                r -= 1
            
            mid = l + (r-l)//2
            
            if nums[mid] > nums[r]:
                l = mid + 1
                
            else:
                r = mid
                
        return nums[l]
      
# DIFFERENT APPROACH

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l<r:
            
            mid = l + (r-l)//2
            
            if nums[mid] > nums[r]:
                l = mid + 1
                
            elif nums[mid] < nums[r]:
                r = mid
            
            else: # nums[mid] == nums[r]
                r -= 1
                
        return nums[l]
