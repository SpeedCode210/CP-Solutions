# Problem: Guess Number Higher or Lower  - https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        a = 1
        b = n
        while True:
            m = (a+b+1)//2
            h = guess(m)
            if h == 0:
                return m
            elif h == 1:
                a = m+1
            else:
                b = m-1
        