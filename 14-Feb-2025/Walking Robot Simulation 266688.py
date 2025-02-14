# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        Ob = set([(x[0],x[1]) for x in obstacles])
        position = (0,0)
        direction = (0,1)
        maxDis = 0
        for c in commands:
            if c == -1:
                direction  = (direction[1], -direction[0])
            elif c == -2:
                direction  = (-direction[1], direction[0])
            else:
                for i in range(c):
                    if not((position[0] + direction[0],position[1] + direction[1]) in Ob):
                        position = (position[0] + direction[0],position[1] + direction[1])
                        maxDis = max(maxDis, position[0]*position[0] + position[1]*position[1])
        return maxDis