class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
            elif prices[i] < minPrice:
                minPrice = prices[i]
        return maxProfit
        