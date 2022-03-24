# https://leetcode.com/problems/contains-duplicate/

# One  method is to use a hashmap (dictionary) to keep track of seen values.

# Another method is to use a set. Set will remove all duplicates since it cannot include duplicate.
# If the len of this set & our array is not the same then it contains duplicates.


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #set removes duplicates
        numsSet = set(nums)
        
        #if there no duplicates then the length should remain the same
        if len(nums) == len(numsSet):
            return False
        else:
            return True
          
          
        
