# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

from collections import deque
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        nums = [nums[i] for i in range(-1, -len(nums)-1,-1)]
        d = deque()
        d.append(nums[0])
        maxi = -1000000000
        for c in nums[1:]:
            if c < maxi:
                return True

            while len(d) > 0 and c > d[0]:
                maxi  = max(maxi, d[0])
                d.popleft()
            if len(d) == 0 or d[0] > c:
                d.appendleft(c)
        return False

        
        
            
