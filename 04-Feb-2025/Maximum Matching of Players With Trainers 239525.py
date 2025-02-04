# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(key=lambda x : -x)
        trainers.sort(key=lambda x : -x)
        p = 0
        for i in range(len(players)):
            if p >= len(trainers):
                continue
            if players[i] <= trainers[p]:
                p += 1
        return p
                
