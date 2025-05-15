# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ps = [0]
        for c in nums:
            ps.append(ps[-1] + c)

        d = deque()
        res = 1000000000
        i = -1
        for c in ps:
            i += 1
            while len(d) > 0 and d[-1][0] >= c:
                d.pop()
            d.append((c,i))
            while d[-1][0] - d[0][0] >= k:
                res = min(res, d[-1][1] - d[0][1])
                d.popleft()
        return res if res != 1000000000 else -1