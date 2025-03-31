# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if(len(people) == 1):
            return 1

        people.sort()
        p0 = 0
        p1 = len(people)-1
        res = 0
        while p0 < p1:
            if people[p1] + people[p0] <= limit:
                res += 1
                p0 += 1
                p1 -= 1
            else:
                res += 1
                p1 -= 1
        if p0 == p1:
            res += 1
        return res