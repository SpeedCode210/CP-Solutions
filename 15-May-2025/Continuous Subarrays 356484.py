# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

from collections import defaultdict
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        cache = []
        res = 0
        p0 = 0
        r = 0
        for c in nums:
            r += 1
            todo = True
            for i in range(len(cache)):
                if cache[i][0] == c:
                    cache[i] = (cache[i][0], cache[i][1]+1)
                    todo = False
            if todo:
                cache.append((c,1))
                cache.sort()

            while cache[-1][0] - cache[0][0] > 2:
                C = nums[p0]
                p0 += 1

                for i in range(len(cache)):
                    if cache[i][0] == C:
                        cache[i] = (cache[i][0], cache[i][1]-1)
                        if cache[i][1] == 0:
                            del cache[i]
                        break

            res += r - p0

        return res