# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean*(len(rolls)+n)
        for u in rolls:
            total -= u
        if 6*n < total or n > total:
            return []
        result = [1]*n
        total -=n
        p = 0
        while total > 0:
            result[p] += min(total, 5)
            p += 1
            total -= min(total, 5)
        return result
