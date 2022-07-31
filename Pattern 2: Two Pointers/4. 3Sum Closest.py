# https://leetcode.com/problems/3sum-closest/

# Solution:
# https://leetcode.com/problems/3sum-closest/discuss/7871/Python-O(N2)-solution

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        
        # len(nums)- 2 because we need at least 3 numbers to continue.
        # it works for len(nums) also because for the last two values l>=r, hence it doesn't enter the while loop.
        for i in range(len(nums) - 2):
            
            l, r = i+1, len(nums) - 1
            
            while l < r:
                
                sum = nums[i] + nums[l] + nums[r]
                
                if sum == target:
                    return sum
                
                # if current difference is less than previous difference
                # update result
                if abs(sum - target) < abs(result - target):
                    result = sum
                    
                # since nums is sorted,
                # get closer to target by shifting the pointers
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                    
        return result
      
      
# Time complexity: O(n^2)
# Space complexity: O(n)


