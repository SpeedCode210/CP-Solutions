# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if len(b) == 0:
            return 1
        return (((a**b[-1])%1337)*(self.superPow(a, b[:-1])**10))%1337