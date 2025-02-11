# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        D = dict()
        for i in range(len(nums)):
            D[nums[i]] = i
        for i in range(len(operations)):
            D[operations[i][1]] = D[operations[i][0]]
            nums[D[operations[i][1]]] = operations[i][1]
        return nums