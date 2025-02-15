# Problem: Python Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right+1):
            found = False
            for k in ranges:
                if i <= k[1] and i >= k[0]:
                    found = True
            if not(found):
                return False
        return True