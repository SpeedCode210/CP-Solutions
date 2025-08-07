# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [0] + [1000000000]*amount

        for i in range(amount+1):
            for c in coins:
                if i-c >= 0:
                    res[i] = min(res[i], 1+res[i-c])

        return res[amount] if res[amount] < 1000000000 else -1