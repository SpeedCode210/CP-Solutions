# Problem: Prime Palindrome - https://leetcode.com/problems/prime-palindrome/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(k):
            if k == 1:
                return False
            i = 2
            while i*i <= k:
                if k%i == 0:
                    return False
                i += 1
            return True

        for i in range(9):
            for j in range(10**(i//2), 10**(i//2 + 1)):
                if i%2 == 1:
                    if int(str(j)+str(j)[-1::-1]) >= n and (isPrime(int(str(j)+str(j)[-1::-1]))):
                        return int(str(j)+str(j)[-1::-1])
                else:
                    if int(str(j)+str(j)[-2::-1]) >= n and (isPrime(int(str(j)+str(j)[-2::-1]))):
                        return int(str(j)+str(j)[-2::-1])