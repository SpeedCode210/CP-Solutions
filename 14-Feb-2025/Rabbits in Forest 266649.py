# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        C = Counter(answers)
        return sum([((C[x]+x)//(x+1))*(x+1) for x in C])
        