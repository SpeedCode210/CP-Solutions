# Problem: Dota2 Senate - https://leetcode.com/problems/dota2-senate/

from collections import Counter
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = [c for c in senate]
        C = Counter(senate)
        i = 0
        d = {"R":0, "D":0}
        while "D" in C and "R" in C and C["R"]*C["D"] > 0:
            if senate[i] == "D":
                if d["D"] > 0:
                    d["D"] -= 1
                    C["D"] -= 1
                    senate[i] = "0"
                else:
                    d["R"] += 1
            elif senate[i] == "R":
                if d["R"] > 0:
                    d["R"] -= 1
                    C["R"] -= 1
                    senate[i] = "0"
                else:
                    d["D"] += 1

            i += 1
            i %= len(senate)

        if C["D"] > 0:
            return "Dire"
        return "Radiant"
