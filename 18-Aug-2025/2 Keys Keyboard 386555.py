# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def __init__(self):
        self.dp = [10000]*10001
        self.dp[1] = 0
    def minSteps(self, n: int) -> int:
        if self.dp[n] != 10000:
            return self.dp[n]
        for i in range(1, n):
            if n%i == 0:
                self.dp[n] = min(self.dp[n], self.minSteps(i) + n//i)
        return self.dp[n]