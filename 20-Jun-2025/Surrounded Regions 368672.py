# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(i, j):
            board[i][j] = 'V'
            res = True
            
            if i < len(board)-1 and board[i+1][j] == 'O':
                res = dfs(i+1, j) and res

            if i > 0 and board[i-1][j] == 'O':
                res = dfs(i-1, j) and res

            if j < len(board[0])-1 and board[i][j+1] == 'O':
                res = dfs(i, j+1) and res

            if j > 0 and board[i][j-1] == 'O':
                res = dfs(i, j-1) and res

            if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1:
                res = False

            return res

        def sec_dfs(i, j):
            board[i][j] = 'X'

            if i < len(board)-1 and board[i+1][j] == 'V':
                sec_dfs(i+1, j)

            if i > 0 and board[i-1][j] == 'V':
                sec_dfs(i-1, j)

            if j < len(board[0])-1 and board[i][j+1] == 'V':
                sec_dfs(i, j+1)
            if j > 0 and board[i][j-1] == 'V':
                sec_dfs(i, j-1)
        
        for i in range(0,len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == 'O':
                    if dfs(i, j):
                        sec_dfs(i, j)

        for i in range(0,len(board)):
            for j in range(0, len(board[0])):
                board[i][j] = board[i][j] if board[i][j] != 'V' else 'O'