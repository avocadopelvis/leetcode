# https://leetcode.com/problems/permutation-in-string/submissions/

# explanation: https://leetcode.com/problems/permutation-in-string/discuss/498216/Python-3-easy-approaches-sorting-hashing-and-rolling-hash

# HASH TABLE METHOD
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        #get count of the characters of s1
        d1 = Counter(s1)
        k = len(s1)
        
        for i in range(len(s2)):
            #get a substring from s2 which is the same length as s1
            sub = s2[i:i+k]
            #get count of the characters of the substring
            d2 = Counter(sub)
            if d1 == d2:
                return True
        
        return False
      
# SORTING | Note: Don't use this as Time Limit Exceeded
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sort s1
        s1 = "".join(sorted(list(s1)))
        k = len(s1)
        
        #sort the substrings of s2 that are of the same size
        for i in range(len(s2)):
            sub = s2[i:i+k] 
            sub_str = "".join(sorted(list(sub)))
            
            if s1 == sub_str:
                return True
            
        return False
      
        
        
