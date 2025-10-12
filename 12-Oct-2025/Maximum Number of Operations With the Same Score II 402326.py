# Problem: Maximum Number of Operations With the Same Score II - https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/

from collections import deque
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        b = [[False]*(len(nums)+1) for _ in range(len(nums)+1)]
        b[0][len(nums)-2] = True
        b[1][len(nums)-1] = True
        b[2][len(nums)] = True
        bfs = deque([(1, 0, len(nums)-2, nums[-1]+nums[-2]), (1, 1, len(nums)-1, nums[-1]+nums[0]), (1, 2, len(nums), nums[0]+nums[1])])

        res = 1

        while len(bfs):
            depth, l, r, s = bfs[0]
            bfs.popleft()
            res = max(res, depth)
            if r-l < 2:
                continue
            
            if not b[l+2][r] and sum(nums[l:l+2]) == s:
                b[l+2][r] = True
                bfs.append((depth+1, l+2, r, s))
            
            if not b[l+1][r-1] and nums[l]+nums[r-1] == s:
                b[l+1][r-1] = True
                bfs.append((depth+1, l+1, r-1, s))
            
            if not b[l][r-2] and sum(nums[r-2:r]) == s:
                b[l][r-2] = True
                bfs.append((depth+1, l, r-2, s))

        return res