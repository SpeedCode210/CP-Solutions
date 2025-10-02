# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distances = [[1000000000]*n for _ in range(n)]
        for i in range(n):
            distances[i][i] = 0
        for x in edges:
            distances[x[0]][x[1]] = x[2]
            distances[x[1]][x[0]] = x[2]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
        
        resu = (n+1, 0)

        for i in range(n):
            resu = min(resu, (len([x for x in distances[i] if x <= distanceThreshold]), -i))
        
        return -resu[1]