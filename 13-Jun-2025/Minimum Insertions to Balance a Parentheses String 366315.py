# Problem: Minimum Insertions to Balance a Parentheses String - https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        res = 0
        for c in s:
            if c == '(':
                if len(stack) > 0 and stack[-1] == 1:
                    res += 1
                    stack.pop()
                stack.append(2)
            else:
                if len(stack) > 0:
                    stack[-1] -= 1
                    if stack[-1] == 0:
                        stack.pop()
                else:
                    stack.append(1)
                    res += 1
        
        return res + sum(stack)
