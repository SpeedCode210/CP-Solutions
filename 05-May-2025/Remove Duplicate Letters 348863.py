# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        print(s)
        S = set()
        last = ""
        ind = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] not in S:
                S.add(s[i])
                last = s[i]
                ind = i
            else:
                if s[i] <= last:
                    ind = i
                    last = s[i]
        if len(S) == 1:
            return last
        return last + self.removeDuplicateLetters("".join([c for c in s[ind+1:] if c != last]))