class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            dist = (x**2 + y**2)

            heapq.heappush(minHeap,(dist,[x,y]))

        ans = []
        
        for i in range(k):
            ans.append(heapq.heappop(minHeap)[1])
        
        return ans