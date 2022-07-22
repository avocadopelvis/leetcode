# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/solution/

# check Search in Rotated Sorted Array solution for further explanation if required

# Since there are duplicate values, we can’t decide which part of the array is sorted. 
# In such a case, the best we can do is to skip one number from both ends: start = start + 1 & end = end - 1.

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
      
      
# This algorithm will run most of the times in O(logN). 
# However, since we only skip two numbers in case of duplicates instead of half of the numbers, the worst case time complexity will become O(N).
# The algorithm runs in constant space O(1).

