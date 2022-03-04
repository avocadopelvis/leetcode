# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        current = start = 0
        minlen = float('inf')
        
        for end in range(len(nums)):
            current += nums[end]
            
            while current >= target:
                minlen = min(minlen, end-start + 1)
                current -= nums[start]
                start += 1
                
        if minlen == float('inf'):
                return 0
        return minlen
