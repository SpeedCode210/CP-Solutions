# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        next_station = [i for i in range(n)]
        flag = [0 for i in range(n)]
        stack = []
        nb_link = 0
        for i in range(n):
            if gas[i] - cost[i] >= 0:
                stack.append(i)
                flag[i] = 1
        i = 0

        while len(stack) > 0:

            i = stack[-1]
            stack.pop()
            nb_link += 1
            next_station[i] = next_station[(i+1)%n]
            w = [next_station[i]]
            while next_station[next_station[i]] != next_station[i]:
                next_station[i] = next_station[next_station[i]]
                w.append(next_station[i])
            for u in w :
                next_station[u] = next_station[i] 
            gas[next_station[i]] += gas[i] - cost[i]
            if gas[next_station[i]] >= cost[next_station[i]] and flag[next_station[i]] == 0:
                stack.append(next_station[i])
                flag[next_station[i]] = 1


        if nb_link == n:
            return (i+1)%n
        return -1