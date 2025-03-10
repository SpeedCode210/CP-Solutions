# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        stack = []
        res = [-1]*len(intervals)
        k = []
        for i in range(len(intervals)):
            k.append((intervals[i][0], 1, i))
            k.append((intervals[i][1], 0, i))
        k.sort()
        for u in k:
            if u[1] == 0:
                stack.append(u[2])
            else:
                for t in stack:
                    res[t] = u[2]
                stack = []
        
        return res