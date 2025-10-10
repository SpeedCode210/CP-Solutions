# Problem: Count Cells in Overlapping Horizontal and Vertical Substrings - https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/description/

class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        pattern = pattern + "?"
        kmp1 = [[0]*len(grid[0]) for _ in range(len(grid))]
        kmp2 = [[0]*len(grid[0]) for _ in range(len(grid))]
        pmp = [0]*len(pattern)
        i = 0
        j = 1
        while j < len(pattern):
            if pattern[i] == pattern[j]:
                i += 1
                pmp[j] = i
                j += 1
            elif i != 0:
                i = pmp[i-1]
            else:
                j += 1

        p = 0
        i,j = 0,0
        while i*len(grid[0]) + j < len(grid)*len(grid[0]):
            if grid[i][j] == pattern[p]:
                p += 1
                kmp1[i][j] = p
                j += 1
            elif p != 0:
                p = pmp[p-1]
            else:
                j += 1
            
            if j == len(grid[0]):
                j = 0
                i += 1

        i,j = 0,0
        p = 0
        
        
        while j*len(grid) + i < len(grid)*len(grid[0]):
            if grid[i][j] == pattern[p]:
                p += 1
                kmp2[i][j] = p
                i += 1
            elif p != 0:
                p = pmp[p-1]
            else:
                i += 1
            
            if i == len(grid):
                i = 0
                j += 1

        C = len(grid[0])
        D = len(grid)
        resu = [[0]*len(grid[0]) for _ in range(len(grid))]
        res = 0
        for i in range(len(grid)*len(grid[0])):
            if kmp1[i//C][i%C] == len(pattern)-1:
                for j in range(i, i-len(pattern)+1, -1):
                    if resu[j//C][j%C]&1:
                        break
                    resu[j//C][j%C] |= 1
                    if resu[j//C][j%C] == 3:
                        res += 1

            if kmp2[i%D][i//D] == len(pattern)-1:
                for j in range(i, i-len(pattern)+1, -1):
                    if resu[j%D][j//D]&2:
                        break
                    resu[j%D][j//D] |= 2
                    if resu[j%D][j//D] == 3:
                        res += 1
        
        return res




        
