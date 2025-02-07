# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        ignore = False
        resu = ""
        for s in source:
            s = s + " "
            i = 0
            while i+1 < len(s):
                if ignore:
                    if s[i:i+2] == "*/":
                        i += 2
                        ignore = False
                    else:
                        i+=1
                else:
                    if s[i:i+2] == "/*":
                        ignore = True
                        i += 2
                    elif s[i:i+2] == "//":
                        if s[i:i+2] == "//":
                            s = s[:i]
                    else:
                        resu = resu + s[i]
                        i+= 1
            if resu != "" and not(ignore):
                res.append(resu)
                resu = ""
        if resu != "" and not(ignore):
            res.append(resu)
            resu = ""
        return res
