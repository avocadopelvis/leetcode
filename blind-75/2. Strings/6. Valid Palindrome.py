# https://leetcode.com/problems/valid-palindrome/

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

# First, we have to make sure to remove all non-alphanumeric characters & all characters are lowercase

# Example of palindrome: radar 

# • Use two pointers
#   left pointer in the beginning & right in the end

# • Make sure the characters are alphanumeric using isalnum()

# • Iterate & Compare values of the pointers
#   If all values are equal then it is a valid palindrome 

# Alternate solution:
# It is shorter but uses extra memory because of new list

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #alternate way but uses extra memory because of new list
        # s = ''.join(c.lower() for c in s if c.isalnum())
        # return s == s[::-1]
        l, r = 0, len(s) - 1
        
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
        return True

      
