# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [0,0]+[1]*(n)
        for i in range(2, n):
            if sieve[i]:
                for j in range(2*i, n, i):
                    sieve[j] = 0
        return sum(sieve[:n])