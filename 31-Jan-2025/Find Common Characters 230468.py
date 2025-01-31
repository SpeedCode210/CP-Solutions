# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        repetitions = {}
        for c in words[0]:
            if c in repetitions :
                repetitions[c] = repetitions[c] + 1
            else :
                repetitions[c] = 1

        for i in range(1,len(words)):
            str_repetitions = {}
            for c in words[i]:
                if c in str_repetitions :
                    str_repetitions[c] = str_repetitions[c] + 1
                else :
                    str_repetitions[c] = 1

            for c in repetitions.keys():
                if c in str_repetitions :
                    repetitions[c] = min(repetitions[c], str_repetitions[c])
                else :
                    repetitions[c] = 0

        result = []
        for c in repetitions.keys():
            for i in range(repetitions[c]):
                result.append(c)
        return result

        