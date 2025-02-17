# Problem: Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        begins = dict()
        ends = dict()
        elements = set()

        for x in nums:
            if x in elements:
                continue
            elements.add(x)
            if x+1 in begins and x-1 in ends:
                b = begins[x+1]
                a = ends[x-1]
                begins.pop(x+1)
                ends.pop(x-1)
                begins[a] = b
                ends[b] = a
            elif x+1 in begins:
                begins[x] = begins[x+1]
                ends[begins[x+1]] = x
                begins.pop(x+1)
            elif x-1 in ends:
                ends[x] = ends[x-1]
                begins[ends[x-1]] = x
                ends.pop(x-1)
            elif not(x in ends) and not(x in begins):
                begins[x] = x
                ends[x] = x

        return max([begins[x] - x + 1 for x in begins])