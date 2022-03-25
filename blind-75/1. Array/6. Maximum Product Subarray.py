# https://leetcode.com/problems/maximum-product-subarray/

# keep track of the current max & current min
# we need current  min also since -ve * -ve is +ve

# current max  = max(current max * n, current min * n, n) #n is also needed since it might be the only +ve/-ve value
# current min = min(current max * n, current min * n, n)    #use temp for current max * n over here
# maximum product = max(maximum product, current max) 


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = currMin = maxPro = nums[0]
        
        for n in nums[1:]:
            temp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(temp, currMin * n, n)
            maxPro = max(maxPro, currMax)
        
        return maxPro
      
      
