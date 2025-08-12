# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        for i in range(query_row):
            print(row)
            row = [max(x-1, 0) for x in row]
            row = [row[0]/2] + [(row[i-1] + row[i])/2 for i in range(1,len(row))] + [row[-1]/2]
        return min(row[query_glass], 1.0)