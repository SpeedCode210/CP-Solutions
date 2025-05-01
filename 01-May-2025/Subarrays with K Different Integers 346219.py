# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        if len(set(nums)) == 1 and k == 1:
            return len(nums)*(len(nums)+1)//2
            
        res = 0
        D = defaultdict(int)
        p1 = 1
        D[nums[0]] += 1
        C = 1
        
        for i in range(len(nums)):
            while C < k and p1 < len(nums):
                D[nums[p1]] += 1
                if D[nums[p1]] == 1:
                    C += 1
                p1 += 1

            if C == k:
                res += 1
                for j in range(p1,len(nums)):
                    if D[nums[j]] > 0:
                        res += 1
                    else:
                        break
            
            D[nums[i]] -= 1
            if D[nums[i]] == 0:
                C -= 1

        return res