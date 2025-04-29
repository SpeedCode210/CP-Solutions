# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def f(self, nums: List[int]):
        if len(nums) == 0:
            return (0,0)
        x = self.f(nums[1:])
        y = self.f(nums[:-1])

        if x[1] + nums[0] > y[1] + nums[-1]:
            return (x[1] + nums[0], x[0])
        return (y[1] + nums[-1], y[0])

    def predictTheWinner(self, nums: List[int]) -> bool:
        return self.f(nums)[0]*2 >= sum(nums)