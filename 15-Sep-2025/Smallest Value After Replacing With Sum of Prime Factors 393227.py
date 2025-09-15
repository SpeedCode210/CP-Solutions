# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        spf = [0,1]+[1000000000]*(2*n)
        for i in range(2,2*n):
            if spf[i] != 1000000000:
                continue
            for j in range(i, 2*n, i):
                spf[j] = min(spf[j], i)
        s = set()
        while n not in s:
            k = 0
            s.add(n)
            while n != 1:
                k += spf[n]
                n = n//spf[n]
            n = k

        return min(s)