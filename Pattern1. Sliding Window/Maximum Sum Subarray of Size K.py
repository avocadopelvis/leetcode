'''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''
# Note: add the element ahead, remove the element at the start of the window

def maxSubarray(self, arr):
  maxSum = windowSum = start = 0
  
  for end in range(len(arr)):
    #add the next element
    windowSum += arr[end]
    
    #slide the window | we don't need to slide if we've not hit the required window size of 'k'
    if end >= k-1: 
      maxSum = max(maxSum, windowSum)
      #subtract the element going out
      windowSum -= arr[start]
      #slide the window ahead
      start += 1
  
  return maxSum

