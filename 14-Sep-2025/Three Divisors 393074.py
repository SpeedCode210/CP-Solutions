# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        i = 2
        while i*i <= n:
            if n%i == 0:
                if i*i < n:
                    return False
                else:
                    return True
            i += 1
        return False