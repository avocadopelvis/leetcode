# https://leetcode.com/problems/two-sum/

# Use dictionary (hashmap) to keep track of the numbers seen (index -> key, value-> value)
	
# • Enumerate the array to get index & value
# • Calculate the remaining i.e target - value (current)
# • If the remaining is in the dictionary then we're done (Since current value + remaining = target)
#   If not then add it to the dictionary (we continue until we find the required remaining for the target)


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        
        for i, value in enumerate(nums):
            remaining = target - value
            
            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[value] = i
