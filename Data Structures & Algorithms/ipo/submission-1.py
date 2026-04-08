class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        buffer = deque()

        totalCapital = w

        for idx,val in enumerate(profits):
            heapq.heappush(heap,(-1 * val,idx))

        while k > 0 and heap:

            #find the first project we are able to do
            while heap and capital[heap[0][1]] > totalCapital:
                val = heapq.heappop(heap)
                buffer.append(val)
            
            #if heap is empty, there are no available projects within our budget
            if not heap:
                return totalCapital
            
            proj = heapq.heappop(heap)

            projProfit = -1* proj[0]

            totalCapital += projProfit

            #empty buffer back into heap:
            while buffer:
                heapq.heappush(heap,buffer.popleft())
            
            k -= 1

        return totalCapital
