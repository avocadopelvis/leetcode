# https://leetcode.com/problems/longest-substring-without-repeating-characters/1

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = maxStr = 0
        seen = set
        
        for r in range(len(s)):
            if s[r] in seen:
                l += 1
            else:
                seen.append(s[r])
                maxStr = max(maxStr, len(seen))
                r += 1
        
        return maxStr
      
