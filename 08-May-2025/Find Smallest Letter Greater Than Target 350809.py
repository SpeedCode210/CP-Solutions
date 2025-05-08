# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        L = sorted(letters)
        if L[-1] <= target:
            return letters[0]
        a = 0
        b = len(letters)-1
        while a < b:
            m = (a+b)//2
            if L[m] > target:
                b = m
            else:
                a = m+1
        return L[a]