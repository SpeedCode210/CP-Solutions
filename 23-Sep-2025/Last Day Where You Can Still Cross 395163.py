# Problem: Last Day Where You Can Still Cross - https://leetcode.com/problems/last-day-where-you-can-still-cross/

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        cells = [(x-1,y-1) for x,y in cells]
        cells.reverse()
        cache = [[1]*col for _ in range(row)]
        bt = [[i for j in range(col)] for i in range(row)]
        uf = [[(i,j) for j in range(col)] for i in range(row)]
        
        def f(i,j):
            h = []
            while (i,j) != uf[i][j]:
                h.append((i,j))
                i,j = uf[i][j]
            for x in h:
                uf[x[0]][x[1]] = (i,j)
            return (i,j)
        
        day = row*col

        for cell in cells:
            cache[cell[0]][cell[1]] = 0
            for u in [(cell[0], cell[1]+1), (cell[0], cell[1]-1), (cell[0]+1, cell[1]), (cell[0]-1, cell[1])]:
                if 0 <= u[0] < row and 0 <= u[1] < col and cache[u[0]][u[1]] == 0:
                    A = f(*cell)
                    B = f(*u)
                    if A[0] > B[0]:
                        A,B = B, A

                    if A != B:
                        uf[B[0]][B[1]] = A
                        bt[A[0]][A[1]] = max(bt[B[0]][B[1]], bt[A[0]][A[1]])
                    if A[0] == 0 and bt[A[0]][A[1]] == row-1:
                        return day-1
            day -= 1
                        