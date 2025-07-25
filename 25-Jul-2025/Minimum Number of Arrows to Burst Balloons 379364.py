# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = [(points[i][0],0, i) for i in range(len(points))] + [(points[i][1], 1,i) for i in range(len(points))] 

        res.sort()

        dead = [0]*len(points)
        alive = []
        slayed = 0
        for x in res:
            if x[1] == 0:
                alive.append(x[2])
            elif not dead[x[2]]:
                slayed += 1
                for x in alive:
                    dead[x] = 1
                alive = []
        return slayed