# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [""]*len(s)
        for i in range(len(s)):
            arr[indices[i]] = s[i]
        return "".join(arr)