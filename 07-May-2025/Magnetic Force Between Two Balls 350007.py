# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        a = 1
        b = position[-1] - position[0]

        def possible(M):
            last = -2*M
            p = 0
            for i in range(m):
                while True:
                    if p == len(position):
                        return False
                    if position[p] - last >= M:
                        last = position[p]
                        break
                    p += 1
            return True

        while a < b:
            M = (a+b+1)//2
            q = -2*m
            if possible(M):
                a = M
            else:
                b = M-1
                
        return a