# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0]*amount

        for x in coins:
            for i in range(1,amount+1):
                if i-x >= 0:
                    dp[i] += dp[i-x]
        return dp[-1]