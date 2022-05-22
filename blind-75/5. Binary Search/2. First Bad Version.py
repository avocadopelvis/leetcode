# https://leetcode.com/problems/first-bad-version/

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n - 1
        
        while l <= r:
            mid = l + (r-l)//2
            #if the mid version is not bad then we start looking in the right side since none of the left side would be bad
            if isBadVersion(mid) == False:
                l = mid + 1
            # if mid version is bad then previous versions are also bad, so we start checking in the left side
            else:
                r = mid - 1
                
        return l
