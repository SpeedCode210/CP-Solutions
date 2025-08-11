# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s) + [1,1]
        dp[len(s)-1] = 0 if s[-1] == '0' else 1
        for i in range(len(s)-2, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
                if s[i] == '1':
                    dp[i] += dp[i+2]
                elif s[i] == '2' and s[i+1] <= '6':
                    dp[i] += dp[i+2]
        return dp[0]