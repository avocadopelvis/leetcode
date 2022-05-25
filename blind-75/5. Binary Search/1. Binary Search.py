# https://leetcode.com/problems/binary-search/solution/

# binary search always left <= right

# look at solution in leetcode for explanation

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = l + (r-l)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1

    
    
