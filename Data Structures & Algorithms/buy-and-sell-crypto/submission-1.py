class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        max_profit = 0

        for price in prices:
            low = min(low, price)

            profit = price - low

            max_profit = max(max_profit, profit)
        
        return max_profit