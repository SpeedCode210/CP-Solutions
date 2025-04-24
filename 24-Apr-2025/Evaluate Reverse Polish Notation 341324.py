# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def ev():
            op = tokens[-1]
            tokens.pop()
            if op in "+-/*":
                a = ev()
                b = ev()

                if op == "+":
                    return a+b
                if op == "-":
                    return b-a
                if op == "/":
                    if a*b < 0:
                        return ((-b)//a)*-1
                    return b//a
                if op == "*":
                    return a*b
            else:
                return int(op)
        res = ev()

        return res