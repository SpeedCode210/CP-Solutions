# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        cache = []
        def f(X : int = 0) -> bool:
            if X == len(num):
                return len(cache) > 2
            if num[X] == '0':
                if len(cache) < 2 or cache[-1]+cache[-2] == 0:
                    cache.append(0)
                    x = f(X+1)
                    if x :
                        return True
                    cache.pop()
                    return x
                else:
                    return False
            for i in range(X+1, len(num)+1):
                if len(cache) >= 2 and int(num[X:i]) != cache[-1]+cache[-2]:
                    continue
                cache.append(int(num[X:i]))
                if f(i):
                    return True
                cache.pop()
            return False
        return f()
                