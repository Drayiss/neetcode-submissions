class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low = prices[0]

        for price in prices:
            profit = price - low
            max_profit = max(max_profit, profit)
            low = min(low, price)
        
        return max_profit
