# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        res = 0
        last = skill[0]+skill[-1]
        for i in range(len(skill)//2):
            if skill[i] + skill[-i-1] != last:
                return -1
            res += skill[i] * skill[-i-1]
        return res