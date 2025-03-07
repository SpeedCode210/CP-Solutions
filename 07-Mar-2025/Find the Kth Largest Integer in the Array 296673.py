# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def f(s):
            return "0"*(100-len(s)) + s
        def minimize(s):
            while len(s) > 1 and s[0:2]== "00":
                s = s[1:]
            return s
        return minimize(sorted(nums, key=f)[-k])