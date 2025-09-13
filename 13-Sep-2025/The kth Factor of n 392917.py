# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        k -= 1
        res = [i+1 for i in range(1000) if n%(i+1) == 0]
        return res[k] if k < len(res) else -1