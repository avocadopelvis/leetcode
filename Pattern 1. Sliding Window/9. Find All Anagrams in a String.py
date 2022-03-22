# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# check out neetcode explanation if confused

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # i -> left pointer | n -> right pointer
        m = len(s)
        n = len(p)
        
        # take count of only the first n characters in s
        sCount = Counter(s[:n])
        pCount = Counter(p)
        
        output = []
        
        for i in range(len(s)):
            if sCount == pCount:
                output.append(i)
                
            #shrink the window
            sCount[s[i]] -= 1
            if sCount[s[i]] <= 0:
                sCount.pop(s[i])
                
            #extend the window
            if n < m:
                # we can take n directly since index starts at 0
                sCount[s[n]] += 1
            
            n += 1
        
        return output
      
      
