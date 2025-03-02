# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        def hi(i,j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return 0
            return board[i][j]%2

        for i in range(len(board)):
            for j in range(len(board[0])):
                somme  = hi(i+0,j+1)
                somme += hi(i+0,j-1)
                somme += hi(i+1,j+1)
                somme += hi(i+1,j-1)
                somme += hi(i+1,j+0)
                somme += hi(i-1,j-1)
                somme += hi(i-1,j+0)
                somme += hi(i-1,j+1)
                if (somme == 2 or somme == 3) and hi(i,j) == 1:
                    board[i][j] += 2
                elif somme == 3:
                    board[i][j] += 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] //= 2