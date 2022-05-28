# https://leetcode.com/problems/insert-interval/

# Collect the intervals strictly left or right of the new interval, then merge the new one with the middle ones (if any) before inserting it between left and right ones.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        
        for i in intervals:
            if i[1] < s:
                left.append(i)
            elif i[0] > e:
                right.append(i)
            else:
                s = min(s, i[0])
                e = max(e, i[1])
                
        return left + [[s, e]] + right

# As we are iterating through all the intervals only once, the time complexity of the above algorithm is O(N), where N is the total number of intervals.
# The space complexity of the above algorithm will be O(N) as we need to return a list containing all the merged intervals.


