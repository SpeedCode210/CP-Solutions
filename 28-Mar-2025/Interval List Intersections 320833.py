# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        k = [(firstList[i][0], 0) for i in range(len(firstList))]  
        k = k + [(firstList[i][1], 1) for i in range(len(firstList))]
        k = k + [(secondList[i][0], 0) for i in range(len(secondList))]
        k = k + [(secondList[i][1], 1) for i in range(len(secondList))]
        k.sort()

        last = k[0]
        count = 1
        for c in range(1, len(k)):
            if count == 2:
                res.append([last[0], k[c][0]])
            count += (1 if k[c][1] == 0 else -1)
            last = k[c]
        return res
