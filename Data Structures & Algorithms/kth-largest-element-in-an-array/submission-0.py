class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap,-num)
        
        val = maxHeap[0]
        for i in range(k):
            val = heapq.heappop(maxHeap)
        return -val