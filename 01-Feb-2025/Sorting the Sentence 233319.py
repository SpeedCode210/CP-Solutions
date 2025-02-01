# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        res_array = ["","","","","","","","",""]
        for word in s.split(" "):
            res_array[int(word[-1])-1] = word[:-1]
        while res_array[-1] == "":
            res_array.pop()
        return " ".join(res_array)
        