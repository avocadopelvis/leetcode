# https://leetcode.com/problems/missing-number/

# set subtraction 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(range(len(nums)+1)) - set(nums)
        return s.pop()
      
      
