class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        maxProfits = []
        for i in range(len(capital)):
            heapq.heappush(heap,(capital[i],profits[i]))

        totalCapital = w

        for _ in range(k):
            if heap and heap[0][0] > totalCapital:
                return totalCapital
            while heap and heap[0][0] <= totalCapital:
                profit = heapq.heappop(heap)[1]
                heapq.heappush(maxProfits,-1*profit)
            # print(f"totalCapital:{totalCapital},  heap:{heap},  maxProfits:{maxProfits}")
            currMaxProfit = -1 * heapq.heappop(maxProfits)
            
            # print(f"adding {currMaxProfit} to total")
            totalCapital += currMaxProfit

        

        return totalCapital
