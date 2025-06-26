# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        graph = [[] for i in range(m*2*n+ m + n)]
        

        def link(a,b):
            graph[a].append(b)
            graph[b].append(a)

        link(0, m)

        for i in range(n):
            for j in range(m):
                left =  j + (2*m+1)*i + m
                right =  j + (2*m+1)*i + m + 1
                top = j + (2*m+1)*i
                bottom = j + (2*m+1)*(i+1)
                if grid[i][j] == 1:
                    link(left, right)
                if grid[i][j] == 2:
                    link(top, bottom)
                if grid[i][j] == 3:
                    link(left, bottom)
                if grid[i][j] == 4:
                    link(right, bottom)
                if grid[i][j] == 5:
                    link(top, left)
                if grid[i][j] == 6:
                    link(top, right)
        

        visited = [False]*(m*2*n+ m + n)
        stack = [0 if grid[0][0] != 4 else m+1]
        visited[0 if grid[0][0] != 4 else m+1] = True

        S = [len(visited)-1, len(visited)-m-1, len(visited)-m-2, len(visited)-1 - 2*m - 1]

        while len(stack):
            s = stack[-1]
            stack.pop()
            for x in graph[s]:
                if s in S and x in S:
                    return True
                if not visited[x]:
                    stack.append(x)
                    visited[x] = True

        return False