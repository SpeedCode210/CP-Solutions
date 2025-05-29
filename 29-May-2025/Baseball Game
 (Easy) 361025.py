# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a = []
        for c in operations:                
            if c == '+':
                a.append(a[-1]+a[-2])
            elif c == 'D':
                a.append(2*a[-1])
            elif c == 'C':
                a.pop()
            else:
                a.append(int(c))
        return sum(a)