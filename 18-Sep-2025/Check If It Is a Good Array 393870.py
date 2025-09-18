# Problem: Check If It Is a Good Array - https://leetcode.com/problems/check-if-it-is-a-good-array/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(a,b):
            if a > b:
                a,b = b,a
            if a == 0:
                return b
            return gcd(a,b%a)
        
        x = 0
        for n in nums:
            x = gcd(x, n)
        
        return x == 1