# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        maxlen = max([len(x) for x in words])
        result = []
        for i in range(maxlen):
            result.append([" "]*len(words))

        for i in range(len(words)):
            for j in range(len(words[i])):
                result[j][i] = words[i][j]
        result = ["".join(x) for x in result]
        for i in range(len(result)):
            k = -1
            while k > -len(result[i]) and result[i][k] == " ":
                k -= 1
            if k < -1:
                result[i] = result[i][:k+1]
        return result