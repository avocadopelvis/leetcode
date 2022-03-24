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

      
