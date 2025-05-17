# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] > arr[1]:
            return False
        flag = False
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            if arr[i] > arr[i-1]:
                if flag :
                    return False
            if arr[i] < arr[i-1]:
                flag = True
        return flag