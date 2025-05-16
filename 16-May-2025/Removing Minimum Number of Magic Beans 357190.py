# Problem: Removing Minimum Number of Magic Beans - https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        pf = [0]
        pf2 = [0]
        for c in beans:
            pf.append(c + pf[-1])
        for c in reversed(beans):
            pf2.append(c + pf2[-1])
        res = 999999999999999999
        for i in range(len(beans)):
            cost = pf[i] + pf2[len(beans) - i-1] - beans[i]*(len(beans)-i-1)
            res = min(res, cost)

        return res
