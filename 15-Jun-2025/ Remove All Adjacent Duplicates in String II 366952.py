# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = []
        a = []
        for c in s :
            if len(a) == 0 or a[-1][0] != c:
                a.append((c, 1))
            else:
                a[-1] = (a[-1][0], a[-1][1] + 1)
                if a[-1][1] == k:
                    a.pop()
        for x in a:
            for i in range(x[1]):
                res.append(x[0])
        return "".join(res)