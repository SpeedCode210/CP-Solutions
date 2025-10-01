# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = [1000000000]*(n+1)

        res[k] = 0

        for i in range(n):
            for t in times:
                res[t[1]] = min(res[t[1]], res[t[0]] + t[2])
        
        res = max(res[1:])

        return res if res < 1000000000 else -1