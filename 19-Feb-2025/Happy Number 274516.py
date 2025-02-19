# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        S = set()
        while True:
            if n == 1:
                return True

            if n in S:
                return False
            else :
                S.add(n)
            
            n = sum([((n//(10**i)) % 10)**2 for i in range(12)])