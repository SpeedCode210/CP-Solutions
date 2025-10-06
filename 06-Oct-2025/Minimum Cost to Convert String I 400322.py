# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

from collections import defaultdict
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        C = defaultdict(lambda : defaultdict(lambda : 1000000000000000000))

        for i in range(len(cost)):
            C[original[i]][changed[i]] = min(C[original[i]][changed[i]], cost[i])
        
        for k in "qwertyuiopasdfghjklzxcvbnm":
            C[k][k] = 0
            for i in "qwertyuiopasdfghjklzxcvbnm":
                for j in "qwertyuiopasdfghjklzxcvbnm":
                    C[i][j] = min(C[i][j], C[i][k] + C[k][j])
        

        total = sum([C[source[i]][target[i]] for i in range(len(source))])

        if total >= 1000000000000000000:
            return -1
        return total
        
