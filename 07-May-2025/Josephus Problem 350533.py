# Problem: Josephus Problem - https://www.geeksforgeeks.org/josephus-problem/

class Solution:
    def josephus(self,n,k):
        if n == 1:
            return 1
        s = [c for c in range((k%n if k%n != 0 else n)+1,n+1)] + [c for c in range(1,(k%n if k%n != 0 else n))]
        return s[self.josephus(n-1, k)-1]