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
            
            if starti <= endj and startj <= endi:
                result.append([max(starti, startj), min(endi, endj)])
            
            # we increment the pointer when one interval is exhausted i.e we used the entire range, so we move on to the next interval
            if endi <= endj:
                i += 1
            else:
                j += 1
                
        return result
    
# As we are iterating through both the lists once, 
# the time complexity of the above algorithm is O(N + M), where N and M are the total number of intervals in the input arrays respectively.
# Ignoring the space needed for the result list, the algorithm runs in constant space O(1).

      
    
            
