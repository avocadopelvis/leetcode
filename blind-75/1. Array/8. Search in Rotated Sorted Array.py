\# https://leetcode.com/problems/search-in-rotated-sorted-array/

# in a rotated sorted array, there will be a left sorted portion and a right sorted portion

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
            
            # check if mid is in left or right sorted portion
            
            # left sorted portion
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]: # check if target is in left sorted portion
                    r = mid - 1
                # since target is not in left sorted portion, we will only search in right sorted portion now
                else:
                    l = mid + 1
            
            # right sorted portion
            else:
                if nums[mid] <= target <= nums[r]: # check if target is in right sorted portion
                    l = mid + 1
                # since target is not in right sorted portion, we will only search in left sorted portion now
                else:
                    r = mid - 1
                    
        return -1
      
