# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

from collections import defaultdict
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        D = defaultdict(int)
        for x in changed:
            D[x] += 1

        changed.sort()
        res = []
        for x in changed:
            if D[x] == 0:
                continue
            D[x] -= 1
            if D[2*x] == 0:
                return []
            else:
                res.append(x)
                D[2*x] -= 1
        return res