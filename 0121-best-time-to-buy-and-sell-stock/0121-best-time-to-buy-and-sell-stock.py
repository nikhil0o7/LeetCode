class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(0, len(prices)):
            if max_profit < prices[i] - min_price:
                max_profit = prices[i] - min_price
            elif min_price > prices[i]:
                min_price = prices[i]
        return max_profit
