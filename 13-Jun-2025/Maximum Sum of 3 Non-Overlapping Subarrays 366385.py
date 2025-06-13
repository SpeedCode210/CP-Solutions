# Problem: Maximum Sum of 3 Non-Overlapping Subarrays - https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        a = [-1]*(k-1) + [sum(nums[:k])]
        for i in range(k, len(nums)):
            a.append(a[-1] + nums[i] - nums[i-k])
        best_sum = [-1]*(k-1)+[k-1]
        for i in range(k, len(nums)):
            best_sum.append(best_sum[-1] if a[best_sum[-1]] >= a[i] else i)
        best_pair = [-1]*(2*k-1) + [[k-1, 2*k-1]]
        for i in range(2*k, len(nums)):
            best_pair.append(best_pair[-1] 
            if  a[best_pair[-1][0]] + a[best_pair[-1][1]] >= a[i] + a[best_sum[i-k]]
            else [best_sum[i-k] , i])

        best_tuple = [-1]*(3*k-1) + [[k-1, 2*k-1, 3*k-1]]
        for i in range(3*k, len(nums)):
            best_tuple.append(best_tuple[-1] 
            if  a[best_tuple[-1][0]] + a[best_tuple[-1][1]] + a[best_tuple[-1][2]] >= a[i] + a[best_pair[i-k][0]] + a[best_pair[i-k][1]]
            else [best_pair[i-k][0] ,best_pair[i-k][1] , i])

        return [x - k + 1 for x in best_tuple[-1]]
        
        
