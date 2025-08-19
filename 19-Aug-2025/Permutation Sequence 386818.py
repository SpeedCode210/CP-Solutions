# Problem: Permutation Sequence - https://leetcode.com/problems/permutation-sequence/description/

class Solution:
    def __init__(self):
        self.permu = [1]
        for i in range(1, 10):
            self.permu.append(self.permu[-1]*i)
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return "1"
        k -= 1
        first = "123456789"[k//self.permu[n-1]]
        res = self.getPermutation(n-1, k%self.permu[n-1] + 1)
        cache = [x for x in "123456789" if x != first]
        resu = [first]
        for i in res:
            resu.append(cache[ord(i) - ord('1')])
        return "".join(resu)
