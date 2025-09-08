# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/description/

class Solution:
    def maximumGap(self, nums: List[int], s = 30) -> int:
        if s < 0:
            return 0
        mask = 1<<s
        for i in range(s,-1,-1):
            h = nums[0] & mask
            mini = -1
            maxi = 1000000001
            m = []
            M = []
            for x in nums:
                if x&mask:
                    maxi = min(maxi, x)
                    m.append(x)
                else:
                    mini = max(mini, x)
                    M.append(x)
            if mini > -1 and maxi < 1000000001:
                return max(maxi-mini, self.maximumGap(m, i-1), self.maximumGap(M, i-1))
            mask >>= 1
        return 0