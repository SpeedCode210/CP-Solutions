# Problem: Reduction Operations to Make the Array Elements Equal - LeetCode - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/

from collections import Counter
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        C = Counter(nums)
        X = sorted([(i, C[i]) for i in C], key = lambda x: -x[0])
        U = [0]
        for i in range(0, len(X)):
            U.append(U[-1] + X[i][1])
        print(U)

        if len(U) == 2:
            return 0
        return sum([x for x in U]) - U[-1]