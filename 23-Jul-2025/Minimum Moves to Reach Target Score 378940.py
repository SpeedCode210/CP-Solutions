# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target == 1:
            return 0
        if maxDoubles == 0:
            return target-1
        if target%2 == 1:
            return 1 + self.minMoves(target-1, maxDoubles)
        return 1 + self.minMoves(target//2, maxDoubles-1)