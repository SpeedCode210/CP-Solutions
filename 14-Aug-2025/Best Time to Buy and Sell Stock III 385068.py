# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-prices[0],-1000000000,-1000000000,-1000000000]]
        res = 0
        for i in range(1, len(prices)):
            dp.append([ max(dp[i-1][0], - prices[i]), max(dp[i-1][1], dp[i-1][0] + prices[i]), max(dp[i-1][2], dp[i-1][1] - prices[i]), max(dp[i-1][3], dp[i-1][2] + prices[i]) ])

        return max(dp[-1] + [0])