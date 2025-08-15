# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0,-1000000000], [0,-1000000000]]
        for x in prices:
            dp.append([max(dp[-1][0], dp[-1][1] + x), max(dp[-1][1], dp[-2][0] - x)])
        return (max(dp[-1]))