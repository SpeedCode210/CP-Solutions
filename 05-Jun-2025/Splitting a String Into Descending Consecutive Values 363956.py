# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def hi(i : int, j : int) -> bool:
            if i == len(s):
                return True
            for k in range(i+1, len(s)+(1 if i > 0 else 0)):
                if (i == 0 or int(s[i:k]) == j-1) and hi(k, int(s[i:k])):
                    return True
            return False


        return hi(0,0)