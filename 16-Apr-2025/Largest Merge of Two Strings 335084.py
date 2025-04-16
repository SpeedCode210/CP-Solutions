# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        arr = []
        p0 = 0
        p1 = 0
        while p0 < len(word1) or p1 < len(word2):
            if p0 == len(word1):
                arr.append(word2[p1])
                p1 += 1
            elif p1 == len(word2):
                arr.append(word1[p0])
                p0 += 1
            else:
                if word1[p0:] > word2[p1:]:
                    arr.append(word1[p0])
                    p0 += 1
                else:
                    arr.append(word2[p1])
                    p1 += 1
               
        return "".join(arr)
