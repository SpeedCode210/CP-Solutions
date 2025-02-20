# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        D = []
        for i in range(len(points)):
            D.append(defaultdict(int))
            for j in range(len(points)):
                D[-1][(points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2] += 1
        return sum([sum([(d[i])*(d[i]-1) for i in d]) for d in D])