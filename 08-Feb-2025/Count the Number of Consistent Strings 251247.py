# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_letters = set()
        for c in allowed:
            allowed_letters.add(c)
        res = len(words)
        for word in words:
            for c in word:
                if not(c in allowed_letters):
                    res -= 1
                    break
        return res
