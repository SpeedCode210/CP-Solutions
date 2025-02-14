# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.nums = defaultdict(int)
        self.repetitions = defaultdict(set)
        

    def add(self, number: int) -> None:
        self.nums[number] += 1
        self.repetitions[self.nums[number]-1].discard(number)
        self.repetitions[self.nums[number]].add(number)

    def deleteOne(self, number: int) -> None:
        if self.nums[number] > 0:
            self.nums[number] -= 1
            self.repetitions[self.nums[number]].add(number)
            self.repetitions[self.nums[number]+1].discard(number)

    def hasFrequency(self, frequency: int) -> bool:
        return len(self.repetitions[frequency]) > 0

        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)