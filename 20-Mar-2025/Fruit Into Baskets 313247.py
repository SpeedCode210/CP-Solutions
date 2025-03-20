# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        p0 = 0
        F = [1,0]
        f = [fruits[0],0]
        p1 = 1
        res = 1
        while p1 < len(fruits):
            if F[0] > 0 and f[0] == fruits[p1]:
                F[0] += 1
            elif F[1] > 0 and f[1] == fruits[p1]:
                F[1] += 1
            elif F[0] == 0:
                F[0] += 1
                f[0] = fruits[p1]
            elif F[1] == 0:
                F[1] += 1
                f[1] = fruits[p1]
            else:
                if F[0] > 0 and f[0] == fruits[p0]:
                    F[0] -= 1
                elif F[1] > 0 and f[1] == fruits[p0]:
                    F[1] -= 1
                p0 += 1
                p1 -= 1
            p1 += 1
            res = max(p1-p0, res)
        return res