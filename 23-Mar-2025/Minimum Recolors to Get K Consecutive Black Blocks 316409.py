# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution(object):
    def minimumRecolors(self, blocks, k):
        res = len([c for c in blocks[:k] if c == "W"])
        count = res
        for i in range(k, len(blocks)):
            count += 1 if blocks[i] == "W" else 0
            count -= 1 if blocks[i-k] == "W" else 0
            res = min(count, res)
        return res

        