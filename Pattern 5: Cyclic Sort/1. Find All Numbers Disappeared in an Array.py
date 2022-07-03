# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# SET SUBTRACTION
# take a set with numbers from the size of the array nums and subtract it with set containing the values in the array nums
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        return set(range(1, len(nums)+1)) - set(nums)
      
      
      
