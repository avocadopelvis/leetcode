# https://leetcode.com/problems/container-with-most-water/

# • Use two pointers (start & end) 

# • Initially maximum area is 0

# • Area = length * width

# • To get length, we take the minimum of height[start] & height[end]

# • width = end - start

# • Keep track of the maximum area in each iteration

# • We move the pointer which has minimum height


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea = 0
        
        while l < r:
            length = min(height[l], height[r])
            width = r - l
            
            area = length * width
            maxArea = max(maxArea, area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return maxArea
      
      
