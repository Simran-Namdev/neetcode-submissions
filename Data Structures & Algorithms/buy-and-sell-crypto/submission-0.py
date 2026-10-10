class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        for r in range(len(prices)):
            p = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            profit = max(p, profit)
        return profit
        