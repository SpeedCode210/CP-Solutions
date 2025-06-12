# Problem: Gray Code - https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0,1]
        x = self.grayCode(n-1)
        return [2*u for u in x] + [2*u+1 for u in reversed(x)]