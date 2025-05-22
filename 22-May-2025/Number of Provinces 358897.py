# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        nb = 0
        visited = [False]*len(isConnected)
        for i in range(len(isConnected)):
            if visited[i]:
                continue
            nb += 1
            dfs = [i]
            while len(dfs) > 0:
                x = dfs[-1]
                dfs.pop()
                for j in range(len(isConnected)):
                    if (isConnected[j][x] or isConnected[x][j]) and not(visited[j]):
                        dfs.append(j)
                        visited[j] = True

        return nb