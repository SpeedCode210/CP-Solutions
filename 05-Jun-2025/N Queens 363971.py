# Problem: N Queens - https://leetcode.com/problems/n-queens/

from copy import deepcopy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.']*n for i in range(n)]
        diffs = [True]*20
        sums = [True]*20
        cols = [True]*10
        def f(level : int):
            if level == n:
                res.append(["".join(x) for x in board])
                return

            for i in range(n):
                board[level][i] = 'Q'
                if diffs[level - i + 10] and sums[level + i] and cols[i]:
                    diffs[level - i + 10] = False
                    sums[level + i] = False
                    cols[i] = False
                    f(level+1)
                    diffs[level - i + 10] = True
                    sums[level + i] = True
                    cols[i] = True
                board[level][i] = '.'

        f(0)
        return res