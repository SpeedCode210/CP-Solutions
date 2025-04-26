# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        cache = [1000000000]*102
        for i in range(len(temperatures)-1, -1, -1):
            answer[i] = min(cache[temperatures[i]+1:]) - i
            if answer[i] > 100003:
                answer[i] = 0
            cache[temperatures[i]] = i
        return answer
