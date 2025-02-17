# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        k = 1000000
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] != list2[j]:
                    continue
                if i+j == k:
                    res.append(list1[i])
                elif i+j < k:
                    k = i+j
                    res = [list2[j]]
        return res