# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack = [[]]
        
        for x in s:
            if x == '(':
                stack.append([])
            elif x == ')':
                stack[-2] += reversed(stack[-1])
                stack.pop()
            else:
                stack[-1].append(x)
                
        return "".join(stack[0])