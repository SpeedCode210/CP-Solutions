# Problem: Find the Index of the First Occurrence in a String - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        prime = 1000000007
        thing = 263

        if len(needle) > len(haystack):
            return -1

        needleHash = 0
        for x in needle:
            needleHash *= thing
            needleHash += ord(x)
            needleHash %= prime
        
        hayHash = 0
        for i in range(len(needle)):
            hayHash *= thing
            hayHash += ord(haystack[i])
            hayHash %= prime

        p = pow(thing, len(needle)-1, prime)

        for i in range(len(needle), len(haystack)):
            if hayHash == needleHash:
                if needle == haystack[i-len(needle): i]:
                    return i-len(needle)
            
            hayHash -= p*ord(haystack[i-len(needle)])
            hayHash *= thing
            hayHash += ord(haystack[i])
            hayHash = ((hayHash%prime)+prime)%prime

        if hayHash == needleHash:
            if needle == haystack[-len(needle):]:
                return len(haystack)-len(needle)

        return -1


