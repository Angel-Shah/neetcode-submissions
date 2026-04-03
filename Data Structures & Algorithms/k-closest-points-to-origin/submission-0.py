import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dist = math.sqrt((x-0)**2 + (y-0)**2)

            heapq.heappush(minHeap,(dist,[x,y]))

        ans = []
        
        for i in range(k):
            ans.append(heapq.heappop(minHeap)[1])
        
        return ans