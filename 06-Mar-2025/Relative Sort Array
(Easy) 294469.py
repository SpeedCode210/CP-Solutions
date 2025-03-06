# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hi = dict()
        for i,x in enumerate(arr2):
            hi[x] = i
        for _ in range(len(arr1)):
            for i in range(len(arr1) - 1):
                if (not(arr1[i] in hi) and arr1[i+1] in hi) or (arr1[i+1] in hi and hi[arr1[i]] > hi[arr1[i+1]]):
                    arr1[i],arr1[i+1] = arr1[i+1],arr1[i]
                elif not(arr1[i] in hi) and not(arr1[i+1] in hi) and arr1[i] > arr1[i+1]:
                    arr1[i],arr1[i+1] = arr1[i+1],arr1[i]
        return arr1

        