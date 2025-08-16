# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        probas = [[0.0]*n for i in range(n)]
        probas[row][column] = 1.0
        for i in range(k):
            new_probas = [[0.0]*n for i in range(n)]
            for x in range(n):
                for y in range(n):
                    for u in [(x+2,y+1), (x-2,y+1), (x+2,y-1), (x-2,y-1), (x+1,y+2), (x-1,y+2), (x+1,y-2), (x-1,y-2)]:
                        if u[0] >= 0 and u[0] < n and u[1] >= 0 and u[1] < n:
                            new_probas[u[0]][u[1]] += probas[x][y]/8
            probas = new_probas
        
        return sum([sum(x) for x in probas])