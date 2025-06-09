# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        D = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        def f(i = 0, p = ''):
            if i  == len(digits):
                res.append(p)
                return
            for x in D[digits[i]]:
                f(i+1, p + x)
        f()
        return res