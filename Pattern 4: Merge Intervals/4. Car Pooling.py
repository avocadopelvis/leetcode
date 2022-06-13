# https://leetcode.com/problems/car-pooling/

# check out neetcode vide for explanation:
# https://www.youtube.com/watch?v=08sn_w4LWEE

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         # O(n) (based on the constraints)
#         passChange = [0] * 1001
        
#         for t in trips:
#             numPass, start, end = t
#             passChange[start] += numPass
#             passChange[end] -= numPass
            
#         currPass = 0            
#         for i in range(1001):
#             currPass += passChange[i]
#             if currPass > capacity:
#                 return False
            
#         return True
        
        # O(logn)
        # sort trips based on starting postion
        trips.sort(key = lambda t: t[1])
        
        minHeap = [] # pair of [end, numPassengers]
        currPass = 0
        
        for t in trips:
            numPass, start, end = t
            
            # check to see if a trip is completed
            # to know if a trip is completed, we compare current trip start postion to previous trip end position
            # if the trip is completed, we subtract the passengers
            while minHeap and minHeap[0][0] <= start:
                currPass -= minHeap[0][1]
                heapq.heappop(minHeap)
                
            currPass += numPass
            if currPass > capacity:
                return False
            
            # add current trip to the minHeap
            heapq.heappush(minHeap, [end, numPass])
            
            
        return True
        
        
