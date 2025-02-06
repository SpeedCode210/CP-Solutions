# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = 0
        for k in nums:
            if k%2 == 0:
                total += k
        ans = []
        for k in queries:
            if nums[k[1]]%2 == 0:
                total -= nums[k[1]]
            nums[k[1]] += k[0]
            if nums[k[1]]%2 == 0:
                total += nums[k[1]]
            ans.append(total)
        return ans