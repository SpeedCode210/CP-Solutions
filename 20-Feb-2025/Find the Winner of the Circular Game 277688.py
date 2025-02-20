# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        S = set()
        u = 0
        for i in range(n - 1):
            for j in range(k):
                u += 1
                if u == n+1:
                    u = 1
                while u in S:
                    u += 1
                    if u == n+1:
                        u = 1
            S.add(u)
        return (set(range(1,n+1)) - S).pop()
