# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        cores = [processorTime[i//4] for i in range(len(tasks))]
        cores.sort()
        tasks.sort(reverse=True)
        return max([cores[i]+tasks[i] for i in range(len(tasks))])