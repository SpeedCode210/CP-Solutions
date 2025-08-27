# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        cost.append(0)
        for i in range(-3, -len(cost)-1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0:2])