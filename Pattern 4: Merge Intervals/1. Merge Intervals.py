# https://leetcode.com/problems/merge-intervals/

# read solution in leetcode for better understanding

# why merged[-1][1]?
# -1 will give the last array. Since we're appending an interval, it will end up in the right and hence become the last array. 
# So in the next iteration, we can take this recently appended interval and compare it with the current interval

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort the intervals on the startTime to ensure a.start <= b.start
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
      
      
# The time complexity of the above algorithm is O(N * logN), where N is the total number of intervals. 
# We are iterating the intervals only once which will take O(N), in the beginning though, since we need to sort the intervals, our algorithm will take O(N * logN).
# The space complexity of the above algorithm will be O(N) as we need to return a list containing all the merged intervals. We will also need O(N) space for sorting 
