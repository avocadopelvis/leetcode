# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/solution/

# check Search in Rotated Sorted Array solution for further explanation if required

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        
        while l<= r:
            
            # shifting to remove duplicate elements
            while l<r and nums[l] == nums[l+1]:
                l += 1
            while l<r and nums[r] == nums[r-1]:
                r -= 1
            
            mid = l + (r-l)//2
            
            if nums[mid] == target:
                return True
            
            # left
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # right
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return False
      
      
