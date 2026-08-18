class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        profit_today = 0
        minprice = prices[0]
        for i in range(len(prices)):
            profit_today = prices[i] - minprice
            maxprofit = max(profit_today, maxprofit)
            minprice = min(prices[i], minprice)
        return maxprofit