# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        #first window
        windowSum = sum(nums[:k])
        maxAverage = windowSum/float(k)
        
        #rest of the windows
        for i in range(len(nums)-k):
            #remove the end
            windowSum -= nums[i]
            #add the new element ahead
            windowSum += nums[i+k]
            
            currentAverage = windowSum/float(k)
            maxAverage = max(maxAverage, currentAverage)
            
        return maxAverage
