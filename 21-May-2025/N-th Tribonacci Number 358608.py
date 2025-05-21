# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def __init__(self):
        self.dp = [-1]*50
    def tribonacci(self, n: int) -> int:
        if self.dp[n] == -1:
            self.dp[n] = min(1,n) if n <= 2 else (self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3))
        return self.dp[n]