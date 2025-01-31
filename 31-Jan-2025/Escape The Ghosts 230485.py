# Problem: Escape The Ghosts - https://leetcode.com/problems/escape-the-ghosts/

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = abs(target[0]) + abs(target[1])
        for ghost in ghosts :
            if abs(target[0] - ghost[0]) + abs(target[1] - ghost[1]) <= distance :
                return False
        return True