class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCost = [-1]*(amount+1)
        minCost[0] = 0#base case

        for x in range(amount+1):
            minCoin = float('inf')
            for c in coins:
                if x >= c:
                    if minCost[x-c] != -1:
                        currCoins = 1 + minCost[x - c]
                        minCoin = min(minCoin,currCoins)
                        minCost[x] = minCoin
        return minCost[-1]
