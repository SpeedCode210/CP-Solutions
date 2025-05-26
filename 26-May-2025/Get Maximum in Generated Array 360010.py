# Problem: Get Maximum in Generated Array - https://leetcode.com/problems/get-maximum-in-generated-array/description/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        m = n
        dp = [0,1] + [-1]*(n-1)
        for i in range(2, n+1):
            dp[i] = dp[i//2] + (0 if i%2 == 0 else dp[i//2+1])

        return max(dp)
        