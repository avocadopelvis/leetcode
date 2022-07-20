# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# EXPLANATION:
# https://www.youtube.com/watch?v=4sQL7R5ySUU&t=508s

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]
    
    # leftBias = True/False | if False then rightBias
    def binarySearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        
        while l <= r:
            mid = l + (r-l)//2
            
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                i = mid
                if leftBias:
                    r = mid - 1
                else:
                    l = mid + 1
                    
        return i
        
        
# Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(log N) 
# where N is the total elements in the given array.
# The algorithm runs in constant space O(1).

