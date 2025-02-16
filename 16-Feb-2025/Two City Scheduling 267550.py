# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum([u[1] for u in costs]) + sum(sorted([u[0]-u[1] for u in costs])[:(len(costs)//2)])
    