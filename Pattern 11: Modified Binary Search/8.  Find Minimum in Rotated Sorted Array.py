# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Explanation
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation
# checkout neetcode solution again

# requires editing

# right sorted portion will have values smaller than left sorted portion

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        
        # DO NOT use left <= right because that would loop forever
        while l < r:
            mid = l + (r-l)//2
            
            # if this holds true then mid is in right sorted portion
            if nums[mid] > nums[r]:
                # we want to be in left sorted portion since smaller numbers are over there
                l = mid + 1

            # mid is in left sorted portion
            else: # nums[mid] <= nums[right]
                # the right side of mid will have numbers greater than mid
                # so we search in the left side of mid
                r = mid
                
        return nums[l]
      
      
      
