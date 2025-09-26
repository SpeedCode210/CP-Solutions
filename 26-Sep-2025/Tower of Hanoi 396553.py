# Problem: Tower of Hanoi - https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1

class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        if n == 0:
            return 0
        return 1 + self.towerOfHanoi(n-1, fromm, aux, to) + self.towerOfHanoi(n-1, aux, to, fromm)