# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s = ["qwertyuiopQWERTYUIOP","asdfghjklASDFGHJKL","zxcvbnmZXCVBNM"]
        res = []
        for word in words:
            x = 0
            for c in word:
                for i in range(3):
                    if s[i].count(c) > 0:
                        x = x | (2**i)
            if x in [1,2,4]:
                res.append(word)
        return res
