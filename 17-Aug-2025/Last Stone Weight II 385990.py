# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        a = set([0])
        for stone in stones:
            a = set([x-stone for x in a]+[x+stone for x in a])
        return min([abs(x) for x in a])