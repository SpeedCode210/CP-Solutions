# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution(object):
    def maxTurbulenceSize(self, arr):
        res = 1
        c = 1
        for i in range(1, len(arr)):
            if c==1 and arr[i-1] != arr[i]:
                c = 2
            elif arr[i] == arr[i-1] :
                c = 1
            elif arr[i-1] > arr[i-2]:
                if arr[i-1] < arr[i]:
                    c = 2
                else:
                    c+=1
            else:
                if arr[i-1] > arr[i]:
                    c = 2
                else:
                    c+=1
            res = max(res, c)
        return res
        