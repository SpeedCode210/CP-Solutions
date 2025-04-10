# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cache = [-1]
        for i in range(len(nums)):
            if nums[i]%2 == 1:
                cache.append(i)
        cache.append(len(nums))
        res = 0
        for j in range(1, len(cache) - k):
            res += (cache[j] - cache[j-1])*(cache[j+k] - cache[j+k - 1])
        print(cache)
        return res