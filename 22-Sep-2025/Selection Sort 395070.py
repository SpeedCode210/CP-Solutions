# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            u = i
            for j in range(i, len(arr)):
                if arr[j] < arr[u]:
                    u = j
            arr[u], arr[i] = arr[i], arr[u]
        return arr