# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

from copy import copy
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = sum(len(word) for word in words)
        original = defaultdict(int)
        for c in chars:
            original[c] += 1
        for word in words:
            allowed_letters = copy(original)
            for c in word:
                if allowed_letters[c] == 0:
                    res -= len(word)
                    break
                else:
                    allowed_letters[c] -= 1
        return res