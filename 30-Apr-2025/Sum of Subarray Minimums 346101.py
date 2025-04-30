# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 1000000007
        res = 0

        stack = [(-1, -10000000000)]

        som = 0

        for i in range(len(arr)):
            while arr[i] < stack[-1][1]:
                som -= (stack[-1][0] - stack[-2][0])*stack[-1][1]
                stack.pop()
            som += (i - stack[-1][0])*arr[i]
            stack.append((i, arr[i]))
            som = ((som)%MOD + MOD)%MOD
            res = ((res+som)%MOD + MOD)%MOD
        return res