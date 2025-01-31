# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        arr = s.split(" ")
        result = ""
        first = True
        for i in range(0,len(arr)):
            take = False
            for c in arr[i]:
                if c != " ":
                    take = True
            if take and arr[i] != "":
                while arr[i][0] == " ":
                    arr[i] = arr[i][1:]
                while arr[i][len(arr[i])-1] == " ":
                    arr[i] = arr[i][:len(arr[i])-2]
                if first:
                    result = arr[i]
                    first = False
                else :
                    result = arr[i] + " " + result

        return result