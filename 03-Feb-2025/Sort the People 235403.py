# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ppl = []
        for i in range(len(names)):
            ppl.append((names[i],heights[i]))
        ppl.sort(key=lambda person: -person[1])
        return [x[0] for x in ppl]