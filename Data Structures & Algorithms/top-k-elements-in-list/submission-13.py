from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        #count the frequency
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        #now we build and maintain a min-heap of size K
        min_heap = []

        for key,val in counts.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap,(val,key))
            else:
                if min_heap[0][0] < val:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap,(val,key))

        #now we empty the min_heap of size-k into a results array to format the return
        result = []
        while min_heap:
            freq,key = heapq.heappop(min_heap)
            result.append(key)
            
        return result