# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        K = []
        def reverse(b):
            for i in range((b+1)//2):
                arr[i], arr[b - i] = arr[b - i], arr[i]
        
        for i in range(len(arr)):
            maxi = 0
            for j in range(len(arr) - i):
                if arr[maxi] < arr[j]:
                    maxi = j
            K.append(maxi+1)
            reverse(maxi)
            K.append(len(arr)-i)
            reverse(len(arr)-i - 1)

        return K