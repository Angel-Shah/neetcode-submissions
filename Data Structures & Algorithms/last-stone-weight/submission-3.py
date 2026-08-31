class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap) > 1:
            heavy1 = -1* heapq.heappop(heap)
            heavy2 = -1* heapq.heappop(heap)
            if heavy1 != heavy2:
                heapq.heappush(heap, -(heavy1-heavy2))
        
        return -heap[0] if heap else 0