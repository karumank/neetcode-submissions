class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        minimum_price = prices[0]
        max_profit = 0

        for current_price in prices[1:]:
            current_profit = current_price - minimum_price
            max_profit = max(max_profit, current_profit)
            minimum_price = min(minimum_price, current_price)
        return max_profit