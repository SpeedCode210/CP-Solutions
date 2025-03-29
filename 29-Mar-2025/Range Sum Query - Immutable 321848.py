# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.p = [0]
        for c in nums:
            self.p.append(self.p[-1] + c)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.p[right+1] - self.p[left]