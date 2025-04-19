# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.prefix = [[0]*(self.m+1) for i in range(self.n+1)]

        for i in range(self.n):
            for j in range(self.m):
                self.prefix[i+1][j+1] = self.prefix[i+1][j] + self.prefix[i][j+1] - self.prefix[i][j] + matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1] + self.prefix[row1][col1] - self.prefix[row1][col2 + 1] - self.prefix[row2 + 1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)