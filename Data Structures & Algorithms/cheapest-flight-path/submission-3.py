class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        #bellman-ford approch
        prices = [float('inf')]* n
        prices[src] = 0
        for i in range(k+1):
            print(prices)
            tempPrices = prices.copy()
            for s,d,p in flights:
                if prices[s] == float('inf'):#haven't reaced yet
                    continue
                if prices[s]+p < tempPrices[d]:
                    tempPrices[d] = prices[s]+p
            prices = tempPrices

        if prices[dst] == float('inf'):
            return -1
        else:
            return prices[dst]