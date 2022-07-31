# https://leetcode.com/problems/3sum/

# Explanation:
# https://www.youtube.com/watch?v=jzZsG8n2R9A

# sort "nums"

# if sum > 0 then decrease it by shifting the right pointer since numbers are sorted
# if sum < 0 then increase it by shifting the left pointer

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            # we don't want to use the same value in the same position twice
            # if a is equal to the previous value, continue to the next iteration of the loop
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i+1, len(nums)-1
            
            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # shifting one pointer is enough since the above 2 conditions will take care of the other pointer
                    l += 1
                    # same value then shift the pointer
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                        
        return res
    
    
# Time complexity: O(n^2)
# Space complexity: O(n)
        
        
                    
