# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        a = [0]*32
        p0 = 0
        res = 0
        for i in range(len(nums)):
            for j in range(32):
                a[j] += (nums[i]//(2**j))%2
                while a[j] > 1:
                    for jp in range(32):
                        a[jp] -= (nums[p0]//(2**jp))%2
                    p0 += 1
            res = max(res, i-p0+1)

        return res