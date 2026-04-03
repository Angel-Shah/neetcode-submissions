class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            maxHeap.append(-1*stone)
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            heavy1 = -1 * heapq.heappop(maxHeap)
            heavy2 = -1 * heapq.heappop(maxHeap)
            if heavy1 != heavy2:
                heapq.heappush(maxHeap, -1*(abs(heavy1-heavy2)))
        
        if maxHeap:
            return -1*maxHeap[0]
        else:
            return 0