# https://leetcode.com/problems/valid-anagram/

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Use Hashmaps (Dictionary)
# Keep count of characters in both strings & compare to see if they're the same.
# Only downside to this method is memory complexity since we create 2 hashmaps

# Alternate Method:
# Sort the strings. If they contain the same characters then on sorting, they should be equal.

# Another quick way is to use Counter() which  is a dict subclass for counting hashable objects.
# Meaning that it’s the same as the first method.


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False      
        
        countS, countT = {}, {}
        
        for c in range(len(s)):
            countS[s[c]] = 1 + countS.get(s[c], 0)
            countT[t[c]] = 1 + countT.get(t[c], 0)
               
        return countS == countT

        
        #return sorted(s) == sorted(t)
        #OR
        #return Counter(s) == Counter(t)
