class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]
        for sell in prices:
            minBuy = min(minBuy, sell)
            maxProfit = max(maxProfit, sell-minBuy)
        return maxProfit        
