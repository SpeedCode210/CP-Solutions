# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxi = 0
        hi = defaultdict(int)
        nb_repetition = 0
        my_sum = 0
        for i in range(k):
            hi[nums[i]] += 1
            my_sum += nums[i]
            if(hi[nums[i]] > 1) :
                nb_repetition += 1
        if nb_repetition == 0:
            maxi = my_sum

        for i in range(k,len(nums)):a
            hi[nums[i]] += 1
            my_sum += nums[i]
            if(hi[nums[i]] > 1) :
                nb_repetition += 1

            if(hi[nums[i-k]] > 1) :
                nb_repetition -= 1
            hi[nums[i-k]] -= 1
            my_sum -= nums[i-k]
            if nb_repetition == 0:
                maxi = max(my_sum, maxi)
        return maxi

        