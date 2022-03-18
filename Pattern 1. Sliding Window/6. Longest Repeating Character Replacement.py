# https://leetcode.com/problems/longest-repeating-character-replacement/

#Note: We don't actually make any replacements. We just calculate the no. of replacements that we can make in a window 

# EXPLANATION:
# 	• Use sliding window
	
# 	• Use hashmap(dictionary) to count the occurrence of each character.
	
# 	• How do we know which character to replace?
# 	  Replace character which occurs less frequently in the sliding window.

# 	• To check if window is valid:
# 	window length - count[most occurring character] = N    (we want to replace a character with the most occurring character)
	
# 	Here N is the no. of characters in the window that we need to replace 
	
# 	Window is valid when N < k (k is the no. of times that we can make replacements) 
# 	This means that the no. of times that we can make replacement should be greater than the no. of characters that we need to replace
	
# 	• Keep track of the maximum size of the sliding window
# 	• When window is invalid, we shift the the left pointer (reduce the sliding window)

# Shortcut:
# Keep track of the max count of the most occurring character
# This will not affect the solution. (Check NeetCode)

#CODE:
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = maxlen = 0
        count = {}
        
        for right in range(len(s)):
            #increment the count of a character
            count[s[right]] = 1 + count.get(s[right], 0)
            
            #if window is not valid i.e N > k, we shrink the window 
            #N = (window length - most occuring character in the window) i.e the no. of characters that we need to replace
            if (right-left+1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
                
            maxlen = max(maxlen, right-left+1)
        
        return maxlen
      
      
