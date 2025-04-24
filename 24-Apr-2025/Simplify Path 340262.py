# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        a = [""]
        for c in path:
            if c == "/":
                if a[-1] != "":
                    a.append("")
            else:
                a[-1] += c

        stack = []

        for x in a:
            if x == ".":
                pass
            elif x == "..":
                if len(stack) > 0:
                    stack.pop()
            elif x != "":
                stack.append(x)
        
        if len(stack) == 0:
            return "/"
        return "/" + "/".join(stack)