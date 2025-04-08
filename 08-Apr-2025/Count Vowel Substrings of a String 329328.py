# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        res = 0
        for i in range(len(word)):
            for j in range(i):
                s = set([c for c in word[j:i+1]])
                if len(s) == 5 and 'a' in s and 'e' in s and 'i' in s and 'o' in s and 'u' in s:
                    res += 1
        return res
