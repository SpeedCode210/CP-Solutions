# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        b = [[False]*n for i in range(m)]
        def explore(x,y, letter):
            if letter == len(word):
                return True
            if x < 0 or y < 0 or x >= m or y >= n:
                return False
            if b[x][y]:
                return False
            if board[x][y] != word[letter]:
                return False
            b[x][y] = True
            if explore(x+1, y, letter+1):
                return True
            if explore(x, y-1, letter+1):
                return True
            if explore(x, y+1, letter+1):
                return True
            if explore(x-1, y, letter+1):
                return True
            b[x][y] = False
            return False
        for i in range(m):
            for j in range(n):
                if explore(i,j,0):
                    return True
        return False