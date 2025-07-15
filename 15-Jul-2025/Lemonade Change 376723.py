# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counts = [0]*30
        for x in bills:
            counts[x] += 1
            if x == 20:
                if counts[10]:
                    x = 10
                    counts[10] -= 1
            if x == 20:
                if counts[5] >= 3:
                    counts[5] -= 3
                else:
                    return False
            if x == 10:
                if counts[5]:
                    counts[5]-=1
                else:
                    return False
        return True