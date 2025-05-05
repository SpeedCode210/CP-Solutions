# Problem: Tower of Hanoi  - https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

# User function Template for python3

class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        if n < 1:
            return 0
        if n == 1:
            return 1
        return self.towerOfHanoi(n-1, fromm, aux, to)*2 + 1
