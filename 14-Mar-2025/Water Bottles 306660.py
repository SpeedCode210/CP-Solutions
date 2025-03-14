# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        somme = 0
        while numBottles >= numExchange:
            somme += numExchange*(numBottles//numExchange)
            x = (numBottles//numExchange)
            numBottles -= numExchange*(numBottles//numExchange)
            numBottles += x
        return somme + numBottles