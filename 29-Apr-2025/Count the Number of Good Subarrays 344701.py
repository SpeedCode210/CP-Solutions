# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        D = defaultdict(int)
        count = 0
        res = 0
        j = 1
        D[nums[0]] = 1
        for i in range(len(nums)):
            while count < k and j < len(nums):
                count += D[nums[j]]
                D[nums[j]] += 1
                j += 1

            if count < k:
                break

            res += len(nums) - j + 1
            D[nums[i]] -= 1
            count -= D[nums[i]]
        return res