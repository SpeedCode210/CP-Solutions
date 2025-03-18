# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        p = n + len([x for x in arr if x == 0]) - 1
        for i in range(n-1, -1, -1):
            if p < n :
                arr[p] = arr[i]
            p -= 1
            if arr[i] == 0:
                if p < n :
                    arr[p] = arr[i]
                p -= 1