# Problem: Digit Operations to Make Two Integers Equal - https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/description/?envType=problem-list-v2&envId=shortest-path

from heapq import heappush, heappop

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        heap = [(n,n)]

        nbDigit = 1
        while 10**(nbDigit) <= n:
            nbDigit += 1

        d = [1000000000000]*(10**nbDigit)
        v = [False]*(10**nbDigit)
        sieve = [True]*(10**nbDigit)
        sieve[0] = False
        sieve[1] = False
        d[n] = n

        for i in range(2, (10**nbDigit)):
            if sieve[i]:
                for j in range(2*i, (10**nbDigit), i):
                    sieve[j] = False

        if sieve[n] or sieve[m]:
            return -1

        for i in range(10**nbDigit):
            if sieve[i]:
                v[i] = True

        while len(heap):
            _d,a = heap[0]
            heappop(heap)
            if v[a]:
                continue
            v[a] = True
            
            for i in range(nbDigit):
                digit = (a//(10**i))%10
                if digit != 9 and (i != nbDigit-1 or digit != 0):
                    N = a + 10**i
                    if N + _d < d[N]:
                        d[N] = N + _d
                        heappush(heap, (d[N], N))
                if digit != 0:
                    N = a - 10**i
                    if N + _d < d[N]:
                        d[N] = N + _d
                        heappush(heap, (d[N], N))

        return d[m] if d[m] < 1000000000000 else -1