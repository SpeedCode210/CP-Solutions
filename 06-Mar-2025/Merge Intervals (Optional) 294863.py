# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        h = []
        for x in intervals:
            h.append((x[0],0))
            h.append((x[1],1))
        h.sort()
        level = 0
        a = -1
        b = -1
        res = []
        for x in h:
            if level == 0:
                a = x[0]
                level += 1
            else:
                if x[1] == 0:
                    level += 1
                else:
                    level -= 1
                    b = x[0]
            if level == 0:
                res.append([a,b])
        return res