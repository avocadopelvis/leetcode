# https://leetcode.com/problems/find-median-from-data-stream/

# Explanation:
# https://leetcode.com/problems/find-median-from-data-stream/discuss/74047/JavaPython-two-heap-solution-O(log-n)-add-O(1)-find

# The length of smaller half is kept to be n / 2 at all time and the length of the larger half is either n / 2 or n / 2 + 1 depending on n's parity.

# comments might not be 100% correct

class MedianFinder:

    def __init__(self):
        #smaller half | max heap (invert min heap) since we want to get max number 
        self.small = []
        #larger half | min heap since we want min number
        self.large = []
        
        # example:
        # in the case that the size of the list is even
        # small = [1, 2]
        # large = [3, 4]
        # get max number from small -> 2
        # get min number from large -> 3
        # calculate median using these two numbers
        
        
    def addNum(self, num: int) -> None:
        # if even, add to large
        if len(self.small) == len(self.large):
            # push the new number into small and pop the "maximum" item from small then push it into large
            # we use -num because heapq in python is a min heap
            # thus we need to invert the values in the smaller half to mimic a "max heap"
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        #if both equal, it obviously means even
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
        
        
