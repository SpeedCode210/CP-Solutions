# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        cost = 0
        nums.sort()
        right = len(nums) - 1
        left = len(nums) - 1
        ans = 1
        while right > 0:
            while cost <= k and left > 0:
                ans = max(ans, right - left + 1)
                left -= 1
                cost += nums[right] - nums[left]
                print(cost)
                
            if cost <= k:
                ans = max(ans, right - left + 1)
            
            right -= 1
            cost -= (nums[right+1] - nums[right])*(right - left + 1)
        return (ans)

