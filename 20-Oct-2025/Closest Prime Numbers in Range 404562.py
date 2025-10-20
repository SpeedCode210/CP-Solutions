# Problem: Closest Prime Numbers in Range - https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [False, False] + [True]*right
        primes = []
        for i in range(2, len(sieve)):
            if sieve[i]:
                if left <= i <= right:
                    primes.append(i)
                for j in range(2*i, len(sieve), i):
                    sieve[j] = False
        
        if len(primes) < 2:
            return [-1, -1]
        j = 0
        for i in range(2, len(primes)):
            if primes[i] - primes[i-1] < primes[j+1] - primes[j]:
                j = i-1
        return primes[j:j+2]