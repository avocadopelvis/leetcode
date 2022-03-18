# https://leetcode.com/problems/max-consecutive-ones-iii/

# solution explanation: https://leetcode.com/problems/max-consecutive-ones-iii/discuss/1304346/Simple-Solution-w-Explanation-or-Sliding-Window-Approach-with-Comments

# CODE:
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = max1s = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                if k == 0:
                    while nums[left] != 0: #if left pointer is 1 then we keep incrementing until we reach a 0
                        left += 1
                    left += 1
                else: 
                    k -= 1
            
            max1s = max(max1s, right-left+1)
            
        return max1s
      
