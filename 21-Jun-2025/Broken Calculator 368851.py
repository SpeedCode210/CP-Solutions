# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue >= target:
            return startValue - target
        res = 0
        while startValue <= target:
            startValue *= 2
            res += 1
        
        yo = startValue - target
        bits = res
        
        for i in range(bits):
            res += yo%2
            yo //= 2

        return res + yo 