# Problem: Fizz Buzz - https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [""]*n
        for i in range(0,n):
            if (i+1)%15 == 0:
                res[i] = "FizzBuzz"
            elif (i+1)%5 == 0:
                res[i] = "Buzz"
            elif (i+1)%3 == 0:
                res[i] = "Fizz"
            else :
                res[i] = str(i+1)
        return res