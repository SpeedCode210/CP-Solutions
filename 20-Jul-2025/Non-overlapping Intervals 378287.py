# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        stack = []
        res = 0
        for x in intervals:
            if len(stack) == 0:
                stack.append(x)
                continue
            if len(stack) == 1:
                if stack[-1][1] >  x[1]:
                    stack = [x]
                    res += 1
                elif stack[-1][1] <=  x[0]:
                    stack.append(x)
                else:
                    res += 1
                continue
            if x[0] < stack[-2][1]:
                res += 1
                continue
            if stack[-1][1] >  x[1]:
                stack[-1] = x
                res += 1
            elif stack[-1][1] <=  x[0]:
                stack.append(x)
            else:
                res += 1
            
        return res
