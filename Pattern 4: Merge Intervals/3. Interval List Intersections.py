# https://leetcode.com/problems/interval-list-intersections/

# check out:
# https://leetcode.com/problems/interval-list-intersections/discuss/647482/Python-Two-Pointer-Approach-%2B-Thinking-Process-Diagrams
# for explanation


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        result = []
        
        while i < len(firstList) and j < len(secondList):
            starti, endi = firstList[i]
            startj, endj = secondList[j]
            
            if starti <= endj and startj  <= endi:
                result.append([max(starti, startj), min(endi, endj)])
                
            if endi <= endj:
                i += 1
            else:
                j += 1
                
        return result
      
      
    
            
