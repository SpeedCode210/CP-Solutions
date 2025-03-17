# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1,p2=0,-1
        s = numbers[p1]+numbers[p2]
        while True:
            if s < target:
                p1 += 1
            elif s > target:
                p2 -= 1
            else:
                return [p1+1,p2+1+len(numbers)]
            s = numbers[p1]+numbers[p2]
