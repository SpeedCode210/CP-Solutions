# Problem: Expression Add Operators - https://leetcode.com/problems/expression-add-operators/description/

class Solution:        
    def addOperators(self, num: str, target: int) -> List[str]:
        op = ['']*(len(num)-1)
        self.res = []
        def search(lvl = 0):
            if lvl == len(num)-1:
                S = ""
                for i in range(2*len(num)-1):
                    if i%2 == 0:
                        S += num[i//2]
                    else:
                        S += op[i//2]
                for i in range(len(S)-1):
                    if S[i] == '0' and S[i+1].isdigit() and (i == 0 or not(S[i-1].isdigit())):
                            return
                if eval(S) == target:
                    self.res.append(S)
                return
            op[lvl] = '+'
            search(lvl+1)
            op[lvl] = '-'
            search(lvl+1)
            op[lvl] = '*'
            search(lvl+1)
            if lvl == 0 or num[lvl] != '0' or op[lvl-1] == '':
                op[lvl] = ''
                search(lvl+1)
        search()
        return self.res