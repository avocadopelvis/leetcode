# https://leetcode.com/problems/maximum-subarray/

# Initialize current sum to zero & maximum sum as the first element (since there might be only one element)

# If sum is ever negative then reset it to zero

# If not then continue adding each element and get the max sum in each iteration


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]
        
        for n in nums:
            if currSum < 0:
                currSum = 0
                
            currSum += n
            maxSum = max(maxSum, currSum)
            
        return maxSum
      
 
