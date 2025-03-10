# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        N = str(num)
        N = sorted([c for c in N], reverse=(N[0] == "-"))
        if N[0] == "0":
            for i in range(len(N)):
                if N[i] != "0":
                    N[0],N[i] = N[i], N[0]
                    break
        return int("".join(N) if N[-1] != "-" else "-" + "".join(N[:-1])) 