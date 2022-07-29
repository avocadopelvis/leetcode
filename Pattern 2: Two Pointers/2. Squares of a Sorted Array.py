# https://leetcode.com/problems/squares-of-a-sorted-array/

# Solution:
https://leetcode.com/problems/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-two-solutions-explained-beats-100

# If we look at the values in the array "nums" both ends "slide down" and converge towards the center of the array. 
# With that understanding, we can use two pointers, one at each end, to iteratively collect the larger square to a list. 
# However, collecting the larger square in a list with list's append, results in elements sorted in descending order. 
# To circumvent this, we need to append to the left of the list. 
# Using a collections.deque() allows us to append elements to the left of answer in O(1) time, maintaining the required increasing order.

# A deque is a double-ended queue in which elements can be both inserted and deleted from either the left or the right end of the queue. 
# An implementation of a deque in Python is available in the collections module.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = collections.deque()
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # get the absolute values of l & r pointers
            # we are taking absolute values since we will compare them
            left, right = abs(nums[l]), abs(nums[r])
            
            if left > right:
                res.appendleft(left * left)
                l += 1
            
            else:
                res.appendleft(right * right)
                r -= 1
                
        return list(res)
        
# The above algorithm’s time complexity will be O(N) as we are iterating the input array only once.
# The above algorithm’s space complexity will also be O(N); this space will be used for the output array.

# Alternative: Use list and reverse in the end

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # get the absolute values of l & r pointers
            # we are taking absolute values since we will compare them
            left, right = abs(nums[l]), abs(nums[r])
            
            if left > right:
                res.append(left * left)
                l += 1
            
            else:
                res.append(right * right)
                r -= 1
                
        # reverse the list to get ascending order
        return res[::-1]
      
      
