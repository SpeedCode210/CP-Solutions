# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        grid = [[0]*(len(grid[0])+2)] + [[0] + x + [0] for x in grid] + [[0]*(len(grid[0])+2)]
        res = 0
        for i in range(len(grid)-1):
            for j in range(len(grid[0])-1):
                res += (grid[i][j] + grid[i][j+1])%2
                res += (grid[i+1][j] + grid[i][j])%2

        return res