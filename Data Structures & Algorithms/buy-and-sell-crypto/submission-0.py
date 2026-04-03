class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_idx = 0
        sell_idx = 1

        while sell_idx < len(prices):
            max_profit = max(max_profit, prices[sell_idx]-prices[buy_idx])
            if prices[sell_idx] < prices[buy_idx]:
                buy_idx = sell_idx
            sell_idx += 1

        return max_profit        
