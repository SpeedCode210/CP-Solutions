# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int, index: int = 0) -> List[List[int]]:
        if index == len(candidates):
            return [[]] if target == 0 else []
        res = []
        for i in range(1000):
            if i*candidates[index] > target:
                break
            x = self.combinationSum(candidates, target - i*candidates[index], index+1)
            for u in x:
                res.append(u + [candidates[index]]*i)
        return res