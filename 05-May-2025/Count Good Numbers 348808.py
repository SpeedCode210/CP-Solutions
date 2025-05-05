# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 5

        return (pow(4, n//2, 1000000007)*pow(5, (n+1)//2, 1000000007))%1000000007
